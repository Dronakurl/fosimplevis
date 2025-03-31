# fosimplevis

Example for visualization of yolo datasets with fiftyone

1. Clone this repo
2. Put your dataset which is in[YoloV5 format](https://docs.voxel51.com/user_guide/dataset_creation/datasets.html#yolov5dataset) in the subfolder datasets/current
3. Start fifyone with the following command:

```bash
./start.sh
```

## Explanation

fiftyone needs a mongoDB database connection.
The start script will start a mongoDB container and then import the dataset and start fiftyone.
