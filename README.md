# How to run Detectron2 on Windows using WSL2 and RTX30xx cards.

(Detectron2)[https://github.com/facebookresearch/detectron2] is Facebook AI Research's next generation software system that implements state-of-the-art object detection algorithms.

Although it is built using a Windows pipeline, there is no official support for it. There are versions of Detectron2 available for Windows, but at the time of writing, these are older versions of the code and have been modified to remove Linux specific code and replace it with Windows specific code. This means you lose out on later features, bug fixes, improvements, etc. that Facebook include.

This tutorial shows how to get the latest version of Detectron2 working on Windows using WSL2 (Windows Subsystem for Linux), and includes steps for running this on the latest NVidia RTX30xx cards.

In addition, I'll show you how to call Detectron2 running inside WSL2 from Anaconda running natively within Windows.

This tutorial has been tested on the following PC build:

* AMD Ryzen 9 CPU
* NVidia RTX3070
* Windows 10 Home Build 21301.rs_prerelease.210123-1645

Most of this information is available on the Microsoft and Nvidia websites, with some information buried in responses to issues on a number of forums, so for those of you wanting to do this, here's all the information in one place.

### Issues

If you have any issues with this, or over time the instructions change, please raise an issue stating the following:

* Your PC build (CPU, Windows version, GPU and anything else relevant)
* What the errors or issues you experienced are
* Any fixes you've tried or implemented

### High level steps

1. Make sure that you backup your PC first. Some of these changes can be breaking (for example, after this I found that some games didn't work).
1. Join the Windows Insider Program, download and install the latest development release of Windows 10 and configure WSL2 (see https://docs.microsoft.com/en-us/windows/win32/direct3d12/gpu-cuda-in-wsl). I've tested with (Ubuntu 20.04LTS)[https://www.microsoft.com/en-gb/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1#activetab=pivot:overviewtab], feel free to try others Linux distributions if you want. **Note, for those of you with RTX cards (including RTX30xx GPUs), you need to install the GeForce driver from https://developer.nvidia.com/cuda/wsl/download.**
1. Once you have Ubuntu installed, launch it so you have a command prompt.
1. *Optional* (Install Anaconda)[https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/linux.html]. You don't need to do this, but I prefer to ensure that I keep versions of Python and libraries seperate for different projects. I also mix and match between (PyTorch)[https://pytorch.org/] and (Tensorflow)[https://www.tensorflow.org/] development, so this helps significantly. 
1. *Optional* Once Anaconda is installed, create and activate a virtual environment. I'm using Python 3.8.5 here.
1. If you're not using Anaconda, please ensure that you have a recent version of Python installed (I'm using Python 3.8.5 here). You may also need to install other Python libraries to complete the rest of this tutorial.
1. 
