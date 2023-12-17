# GNS3 Project Repository

Welcome to the GNS3 project repository! This repository contains network simulation configurations and router templates for use with the GNS3 network emulator. These projects contain CCNA + CCNP labs from the following resources:
- GNS3Vault: https://gns3vault.com/labs
- NetworkLessons: https://networklessons.com/
- David Bombal CCNP Labs: https://www.youtube.com/watch?v=cck5WO_KaDA&list=PLhfrWIlLOoKNnoF681YXBGs1WdumBYiWJ&ab_channel=DavidBombal

## Directory Structure

- **/configs**: This directory contains GNS3 project files (.gns3) with pre-configured network topologies.
- **/router_templates**: Here you can find templates for various router types that can be imported into GNS3.

## Getting Started

To get started with the GNS3 simulations in this repository, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine using the following command in your folder directory:

```bash
git clone https://github.com/SPACE-AlyeN6378/GNS3-Labs
```

### 2. Import GNS3 Configurations

Open GNS3 on your local machine. If you haven't installed GNS3 yet, [watch this video here](https://www.youtube.com/watch?v=Ibe3hgP8gCA&list=PLhfrWIlLOoKNFP_e5xcx5e2GDJIgk3ep6&ab_channel=DavidBombal). 
Load a project by selecting "File" -> "Open Project" and navigating to the /configs directory within the cloned repository.
The GNS3 project should now be loaded with the pre-configured network topology.

### 3. Install GNS3 VM
For more realistic simulations, it's recommended to use the GNS3 VM. Follow these steps to set it up:

Download the GNS3 VM from GNS3 Download Page.
Import the VM into your preferred virtualization software (e.g., VirtualBox, VMware).

*If you want to use VirtualBox, I highly recommend you to [watch this video here](https://youtu.be/8VQ8eTmMtjQ).*

Configure GNS3 to use the GNS3 VM by going to "Edit" -> "Preferences" -> "GNS3 VM" and selecting the imported VM.

### 4. Install Router Templates
1. First download the Cisco Router/Switch images here: [Download](https://drive.google.com/drive/folders/1FX-oMUTm_Z5Emj-GoUMYAqkNhRXfExU7?usp=drive_link)
2. In GNS3, open the Devices dock on the left click on "Add Template" at the bottom
3. Select the recommended option "Install an appliance from the GNS3 server" and hit Next
4. Select the appliance you have chosen, and click Next
5. Select the recommended option  (i.e. GNS3 VM) and hit Next
6. Once the required image you downloaded is found by GNS3, you're ready to install the appliance
7. And you're all set!

### 5. Start Simulations
With the configurations loaded and router templates installed, you are ready to start your GNS3 simulations. Have fun experimenting with different network scenarios!

## Contributing
Feel free to contribute to this repository by adding new configurations, templates, or improving existing ones. Fork the repository, make your changes, and submit a pull request.

Happy networking!
