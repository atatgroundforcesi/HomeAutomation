
# YAML Documentation

## SupportedTags

## mode

#### Supports Image and VM

**Only one mode can be selected**.

Select your vm or image build. If you are selecting image, some Tags are not required.

**vm**: You can use a single or multiple machine build
**image**: only a single build is allowed. Tag build-type is not allowed. Else an Error while Reading your YAML file will occur

 ```yaml
mode: vm
mode: image
```
## build-type

#### Supports only VM

**Only one build type can be selected**.

(!) If you are creating multiple Machines be sure that every array should contain the same amout of items (!)

Reason is the architecture for multiple builds. The first Item of name and ip defines the name and the ip for the first machine. For the other elements same procedure.

**single**: Only one Machine will be created. Specify only one item in each array or Enter ID Tag to specify which Machine you want to create form your Array

**cluster**: cluster machines are all in the same network. Please only specify network and the address Range of the Machines. 

(!) Be Aware that your Range of Address should match at least your specified Range. Otherwise your Build will fail.

 ```yaml
build-type: single
build-type: multiple
build-type: cluster
```
## name

#### Supports Image and VM

Enter your Names of your VM's or your Image

(!) If there are multiple names set for your Image, There will be thrown an Error while Reading YAML configuration (!)

Reason is the architecture for multiple builds. The first Item of name and ip defines the name and the ip for the first machine. For the other elements same procedure.

**name**: For single or multiple Machine leave name tag empty. Name could only be set for cluster items (*buildtype: cluster* is required). 

 ```yaml
build-type: multiple
name: 
  - dev-ubuntu1
  - dev-ubuntu2
  - dev-ubuntu2

build-type: cluster
name: ubuntu-clu01
  - dev-ubuntu1
  - dev-ubuntu2
  - dev-ubuntu2

#Markdown life Check
#https://markdown-it.github.io/