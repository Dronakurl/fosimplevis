from pathlib import Path

import fiftyone as fo

name = "drone"
dataset_dir = Path(__file__).parent / "datasets" / "current"

if name in fo.list_datasets():
    fo.delete_dataset(name)

dataset = fo.Dataset.from_dir(
    name=name,
    dataset_dir=dataset_dir,
    dataset_type=fo.types.YOLOv5Dataset,
)
print(dataset)

session = fo.launch_app(dataset)
session.wait(-1)
