# How to run Detectron2 on Windows using WSL2 and RTX30xx cards.

(Detectron2)[https://github.com/facebookresearch/detectron2] is Facebook AI Research's next generation software system that implements state-of-the-art object detection algorithms.

Although it is built using a Windows pipeline, there is no official support for it. There are versions of Detectron2 available for Windows, but at the time of writing, these are older versions of the code and have been modified to remove Linux specific code and replace it with Windows specific code. This means you lose out on later features, bug fixes, improvements, etc. that Facebook include.

This tutorial shows how to get the latest version of Detectron2 working on Windows using WSL2 (Windows Subsystem for Linux), and includes steps for running this on the latest NVidia RTX30xx cards.

In addition, I'll show you how to call Detectron2 running inside WSL2 from Anaconda running natively within Windows.

This tutorial has been tested on the following PC build:

* AMD Ryzen 9 CPU
* NVidia RTX3070
* Windows 10 Home Build 21301.rs_prerelease.210123-1645

For this, we will install:

* Ubuntu 20.04LTS
* CUDA 11.2
* Pytorch 1.7.1
* PyCocoTools 2.0.2

Most of this information is available on the Microsoft and Nvidia websites, with some information buried in responses to issues on a number of forums, so for those of you wanting to do this, here's all the information in one place.

** Note that for this tutorial, I'm assuming that you already have a good understanding of Windows, Linux and Python.**

### Issues

If you have any issues with this, or over time the instructions change, please raise an issue stating the following:

* Your PC build (CPU, Windows version, GPU and anything else relevant)
* What the errors or issues you experienced are
* Any fixes you've tried or implemented

### High level steps

1. Make sure that you backup your PC first. Some of these changes can be breaking (for example, after this I found that some games didn't work).
1. Join the Windows Insider Program, download and install the latest development release of Windows 10 and configure WSL2 (see https://docs.microsoft.com/en-us/windows/win32/direct3d12/gpu-cuda-in-wsl). I've tested with (Ubuntu 20.04LTS)[https://www.microsoft.com/en-gb/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1#activetab=pivot:overviewtab], feel free to try others Linux distributions if you want. **Note, for those of you with RTX cards (including RTX30xx GPUs), you need to install the GeForce driver from https://developer.nvidia.com/cuda/wsl/download.** For this step, you'll need to create an NVidia developers account.
1. Once you have Ubuntu installed, launch it so you have a command prompt.
1. *Optional* (Install Anaconda)[https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/linux.html]. You don't need to do this, but I prefer to ensure that I keep versions of Python and libraries seperate for different projects. I also mix and match between (PyTorch)[https://pytorch.org/] and (Tensorflow)[https://www.tensorflow.org/] development, so this helps significantly. 
1. *Optional* Once Anaconda is installed, create and activate a virtual environment. I'm using Python 3.8.5 here.
1. If you're not using Anaconda, please ensure that you have a recent version of Python installed (I'm using Python 3.8.5 here). You may also need to install other Python libraries to complete the rest of this tutorial.
1. You can now test whether your install is working by running `nvidia-smi` from within Ubuntu. You should see the usage statistics for your GPU.
1. Within your Python environment, install the following packages (`conda` instructions below, use `pip` if you need to):
  1. Install pytorch and associated libraries: `conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch`
  1. Install (PyCocoTools)[https://anaconda.org/conda-forge/pycocotools] using `conda install -c conda-forge pycocotools`
1. From Python, check the install by running the following commands. If you get any errors here, please revisit the above steps, and check with the relevant forums for any errors you might get:
  1. `import torch`
  1. `torch.cuda.is_available()` should return `True`. If you get false, please revisit the above steps.
  1. `import pycocotools`
1. You can either install Detectron2 straight from [https://github.com/facebookresearch/detectron2] or clone the repo locally and install from there. In either case, follow the instructions here to (build Detectron2 from source)[https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md#build-detectron2-from-source].
1. Now check that Detectron2 has installed by running `import detectron2` from within Python.

If you've got this far, then Detectron2 is installed and ready for you to use.

### Calling Detectron2 from by API

Detectron2, at the time of writing, does not have a native API. This is simple to setup using (Flask)[https://pypi.org/project/Flask/].

I've provided an (example script)[https://github.com/markstrefford/running-detectron2-on-windows-wsl2-rtx30xx/blob/main/web-api.py] to get you started. **Note that this isn't production ready, it's purely for development and test purposes. This example code isn't designe to handle multiple concurrent requests, etc.**

To call the API, please see this notebook.

You'll notice that these scripts use the (Blosc library)[http://python-blosc.blosc.org/]. This is to facilitate transfering binary (image) data over HTTP inside a JSON request/response.
