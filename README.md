<h1 align="center"> AgentVision2.0</h1>

<div align="center">
<img src="src/docs/images/agentvision.png" >
</div>

AgentVision is a three-headed bot. Each head has it's own objective.

Head 1. Prediction of given classes from the input image <br/>
Head 2. Prediction of Depth Map<br/>
Head 3. Prediction of planar surfaces in the region<br/>

#### Directory structure
```
├───logs
├───resources
└───src
    ├───agentvision
    │   ├───midas
    │   │   ├───midas
    │   │   └───tf
    │   │       ├───input
    │   │       └───output
    │   ├───planercnn
    │   │   ├───anchors
    │   │   ├───datasets
    │   │   ├───data_prep
    │   │   │   └───Renderer
    │   │   ├───example_images
    │   │   └───models
    │   └───yolov3
    │       ├───.github
    │       │   ├───ISSUE_TEMPLATE
    │       │   └───workflows
    │       ├───cfg
    │       ├───data
    │       ├───utils
    │       └───weights
    ├───config
    ├───docs
    │   └───images
    ├───input
    ├───notebook
    └───output
```

**Description:** agentvision contains three models which corresponds to three heads.
1. Yolov3: for Object Detection
2. MiDaS: for Depth maps
3. PlaneRCNN: for Planar regions

These three models were copied from the source and connected as one Encoder-Decoder model. 
src\docs\images
<h4 align="center"> Encoder - Decoder Architecture </h4>

<div align="center">
<img src="src/docs/images/architecture.png" >
</div>
