import shutil
from pathlib import Path


def download_amazon_sales_dataset(
    *, raw_data_dir: Path, kaggle_dataset: str, raw_subdir: str, raw_filename: str
) -> Path:
    target_dir = raw_data_dir / raw_subdir
    target_dir.mkdir(parents=True, exist_ok=True)
    existing_dataset = target_dir / raw_filename

    try:
        import kagglehub
    except ImportError as exc:
        if existing_dataset.exists():
            print(f"kagglehub não instalado. Usando dataset local existente em: {existing_dataset}")
            return target_dir
        raise ImportError(
            "kagglehub não instalado e não existe dataset local em data/raw. "
            "Execute: pip install kagglehub"
        ) from exc

    print(f"Baixando dataset '{kaggle_dataset}' via kagglehub...")
    source_path = Path(kagglehub.dataset_download(kaggle_dataset))

    for item in source_path.iterdir():
        destination = target_dir / item.name
        if item.is_dir():
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    print(f"Download concluido. Arquivos em: {target_dir}")
    return target_dir
