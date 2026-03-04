from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SALES_PATH = ROOT / "modules" / "analise-vendas-python" / "dados_processados" / "vendas_simples.csv"
CUSTOMER_PATH = (
    ROOT / "modules" / "revenue-intelligence" / "data" / "raw" / "E-commerce Customer Behavior - Sheet1.csv"
)
MODEL_METRICS_PATH = ROOT / "modules" / "revenue-intelligence" / "data" / "processed" / "metrics_report.json"
OUTPUT_DIR = ROOT / "reports" / "showcase"


def build_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    risk = df.copy()
    risk["Days Since Last Purchase"] = pd.to_numeric(
        risk["Days Since Last Purchase"], errors="coerce"
    ).fillna(0)
    risk["Total Spend"] = pd.to_numeric(risk["Total Spend"], errors="coerce").fillna(0)
    risk["Satisfaction Level"] = risk["Satisfaction Level"].fillna("Neutral")

    sat_weight = risk["Satisfaction Level"].map(
        {"Unsatisfied": 1.0, "Neutral": 0.7, "Satisfied": 0.35}
    ).fillna(0.5)
    recency_weight = (
        risk["Days Since Last Purchase"] / max(risk["Days Since Last Purchase"].max(), 1)
    ).fillna(0)
    spend_weight = (risk["Total Spend"] / max(risk["Total Spend"].max(), 1)).fillna(0)

    risk["Risk Score"] = (0.5 * recency_weight + 0.35 * sat_weight + 0.15 * spend_weight).clip(0, 1)
    risk["Revenue at Risk (USD)"] = (risk["Total Spend"] * risk["Risk Score"]).round(2)
    risk["Recommended Action"] = risk["Risk Score"].apply(
        lambda x: "Executive Save Offer"
        if x >= 0.8
        else ("CSM Priority Call" if x >= 0.6 else "Nurture Campaign")
    )
    return risk


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sales_df = pd.read_csv(SALES_PATH)
    sales_df["ORDERDATE"] = pd.to_datetime(sales_df["ORDERDATE"], errors="coerce")
    sales_df["SALES"] = pd.to_numeric(sales_df["SALES"], errors="coerce").fillna(0)
    sales_df = sales_df.dropna(subset=["ORDERDATE"]).copy()
    sales_df["month"] = sales_df["ORDERDATE"].dt.to_period("M").astype(str)
    monthly_revenue = sales_df.groupby("month", as_index=False)["SALES"].sum().sort_values("month")

    if len(monthly_revenue) >= 2:
        monthly_revenue["nrr_proxy"] = (
            monthly_revenue["SALES"] / monthly_revenue["SALES"].shift(1)
        ).fillna(1.0).clip(lower=0.6, upper=1.2)
    else:
        monthly_revenue["nrr_proxy"] = 1.0

    customer_df = pd.read_csv(CUSTOMER_PATH)
    risk_df = build_risk_score(customer_df)
    top_actions = risk_df.sort_values("Revenue at Risk (USD)", ascending=False).head(50).copy()

    with MODEL_METRICS_PATH.open("r", encoding="utf-8") as fp:
        model_metrics = json.load(fp)

    summary = {
        "latest_month": monthly_revenue["month"].iloc[-1] if not monthly_revenue.empty else None,
        "latest_revenue_usd": float(monthly_revenue["SALES"].iloc[-1]) if not monthly_revenue.empty else 0.0,
        "nrr_proxy_latest": float(monthly_revenue["nrr_proxy"].iloc[-1]) if not monthly_revenue.empty else 1.0,
        "gross_churn_proxy_latest": float(
            max(0.0, 1 - monthly_revenue["nrr_proxy"].iloc[-1])
        )
        if not monthly_revenue.empty
        else 0.0,
        "total_value_at_risk_usd": float(risk_df["Revenue at Risk (USD)"].sum()),
        "top_50_value_at_risk_usd": float(top_actions["Revenue at Risk (USD)"].sum()),
        "churn_auc_temporal_test": float(
            model_metrics.get("churn", {}).get("temporal_test_roc_auc", 0.0)
        ),
        "next_purchase_auc_temporal_test": float(
            model_metrics.get("next_purchase_30d", {}).get("temporal_test_roc_auc", 0.0)
        ),
    }

    monthly_revenue.to_csv(OUTPUT_DIR / "monthly_revenue.csv", index=False)
    top_actions.to_csv(OUTPUT_DIR / "top_actions.csv", index=False)
    with (OUTPUT_DIR / "summary.json").open("w", encoding="utf-8") as fp:
        json.dump(summary, fp, indent=2)

    print("Showcase demo artifacts generated:")
    print(f"- {OUTPUT_DIR / 'monthly_revenue.csv'}")
    print(f"- {OUTPUT_DIR / 'top_actions.csv'}")
    print(f"- {OUTPUT_DIR / 'summary.json'}")


if __name__ == "__main__":
    main()
