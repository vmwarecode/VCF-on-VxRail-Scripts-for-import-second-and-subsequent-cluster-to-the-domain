INTRODUCTION:
------------

This module contains script files to create a cluster.


REQUIREMENTS:
------------

This module requires the following modules:

  * Python 3 Libraries
  * requests
  * sys
  * json
  * time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.


USAGE:
-----

Sample specification file "cluster_creation_spec_vxrail.json" will be used for cluster creation operation.
For more information on the provided sample file, please refer to API reference documentation.

Usage:  python3 create_cluster_vxrail.py <hostname> <username> <password>

Example: python3 create_cluster_vxrail.py localhost administrator@vsphere.local VMware123!
