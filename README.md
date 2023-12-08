# System Setup Guide

Welcome to the updated setup guide for our system. This document will guide you through the process of setting up the application on your computer.

The following instructions were **run in a Windows machine with RTX-3080 GPU with 10GB of VRAM**.

## Pre-requisites

1. **Computer with GPUs**: Necessary for optimal performance.
2. **Node.js**: Must be installed on your computer. [Download Node.js](https://nodejs.org/)
3. **Python**: Should be installed and operational (tested with Python 3.11.5). [Download Python](https://www.python.org/downloads/)
4. **Conda**: Install conda to create a new environment. Create a new environment for this project. [Download Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
5. **PyTorch**: Must be installed on your computer with CUDA support directly in the generated environment. [Download Pytorch](https://pytorch.org/get-started/locally/)

## Environment Setup

### Back-End Setup

1. **Navigate to Back-End Directory**: Go to the directory with the back-end code `cd backend`.
2. **Install manually Auto-GPT for the Llama Model**: Run the following command.
```
pip3 install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/  # Use cu117 if on CUDA 11.7
```
3. **Install manually the *mmdetection* library**: Run the following command.
```
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
mim install mmdet
```
4.**Replicate Environment**: To create an environment that matches our setup run `pip install -r requirements.txt` to build the dependencies for the environment.


### Front-End Setup

1. **Navigate to Front-End Folder**: Move to the directory containing the front-end code.
2. **Install Node.js Dependencies**: Run `npm install` to install the dependencies listed in `package.json`.

## Preparing the Models

- **Download Pre-Trained Weights**: Ensure you have the necessary pre-trained weights for the models.
To download the weights for the Grounding Dino, run the following commands:
```
cd backend/recipes
mkdir weights
cd weights
wget https://download.openmmlab.com/mmdetection/v3.0/grounding_dino/groundingdino_swinb_cogcoor_mmdet-55949c9c.pth
```

## Running the Application

### Starting the Front-End

1. **Open a Terminal Window**: This will be for the front-end.
2. **Navigate to Frontend Directory**: Use `cd frontend` or the appropriate path.
3. **Run Front-End Server**: Execute `npm run serve`. This will provide a URL to access the front-end, usually hosted on localhost.

### Starting the Back-End

1. **Open Another Terminal Window**: This is for the back-end.
2. **Navigate to Backend Folder**: Use `cd backend` or the appropriate path.
3. **Activate Conda Environment**: Run `conda activate [your_env_name]`, replacing `[your_env_name]` with the name of the created environment.
4. **Run Django API**: Execute `python manage.py runserver` to start the back-end service, which provides a URL.

## Accessing the Web Application

1. **Go to Front-End URL**: Open the URL provided by the front-end in a browser.
2. **Login Page**: If not redirected automatically, add `/login` to the localhost URL.
3. **Login Details**: Use username `admin` and password `1234`.
4. **Initial Page**: After logging in, you'll be directed to the initial page for uploading pictures and generating recipes.

## Additional Features

- **History and Bookmarks**: Access your recipe history and bookmarks from the top navigation bar.

Enjoy your experience with the application and happy cooking!

---

**Note**: This guide presumes a basic understanding of terminal usage and directory navigation. If you encounter issues, please consult the documentation for Node.js, Python, Conda, or your operating system.
