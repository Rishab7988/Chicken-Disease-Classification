from dataclasses import dataclass
from pathlib import Path

# this is the custom datatype
# these are fetched from config.yaml
# frozen=True means the objects of the class can't be modified
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path