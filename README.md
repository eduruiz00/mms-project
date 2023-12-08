Certainly, here's the README.md content as a markdown formatted code snippet:

```markdown
# System Setup Guide

Welcome to the updated setup guide for our system. This document will guide you through the process of setting up the application on your computer, now using an `environment.yml` file to replicate our conda environment for the back-end.

## Pre-requisites

1. **Computer with GPUs**: Necessary for optimal performance.
2. **Node.js**: Must be installed on your computer.
3. **Python**: Should be installed and operational.
4. **Conda**: Required for environment replication.

## Environment Setup

### Front-End Setup

1. **Navigate to Front-End Folder**: Move to the directory containing the front-end code.
2. **Install Node.js Dependencies**: Run `npm install` to install the dependencies listed in `package.json`.

### Back-End Setup

1. **Navigate to Back-End Directory**: Go to the directory with the back-end code.
2. **Replicate Conda Environment**: Use `environment.yml` to create an environment that matches our setup. Run `conda env create -f environment.yml` to build the environment.

## Preparing the Models

- **Download Pre-Trained Weights**: Ensure you have the necessary pre-trained weights for the models.

## Running the Application

### Starting the Front-End

1. **Open a Terminal Window**: This will be for the front-end.
2. **Navigate to Frontend Directory**: Use `cd frontend` or the appropriate path.
3. **Run Front-End Server**: Execute `npm run serve`. This will provide a URL to access the front-end, usually hosted on localhost.

### Starting the Back-End

1. **Open Another Terminal Window**: This is for the back-end.
2. **Navigate to Backend Folder**: Use `cd backend` or the appropriate path.
3. **Activate Conda Environment**: Run `conda activate [your_env_name]`, replacing `[your_env_name]` with the name of the environment created from `environment.yml`.
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
```