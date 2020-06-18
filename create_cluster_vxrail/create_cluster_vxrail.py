#Create Cluster
import sys
import os
import time
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils


class CreateCluster:
    def __init__(self):
        print('Create Clusterr')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def create_cluster(self):
        data = self.utils.read_input(os.path.abspath(__file__ +'/../')+'/cluster_creation_spec_vxrail.json')
        validations_url = 'https://'+self.hostname+'/v1/clusters/validations'
        response = self.utils.post_request(data, validations_url)
        print ('Validatin started for cluster. The valdidation id is: '+ response['id'])
        validate_poll_url = 'https://'+self.hostname+'/v1/clusters/validations/' + response['id']
        print ('Polling on validation api ' + validate_poll_url)
        time.sleep(10)
        validation_status = self.utils.poll_on_id(validate_poll_url, False)
        print('Validate cluster ended with status: ' + validation_status)
        if validation_status != 'SUCCEEDED':
            print ('Validation Failed.')
            exit(1)
        create_cluster_url = 'https://' + self.hostname + '/v1/clusters'
        response = self.utils.post_request(data, create_cluster_url)
        print ('Creating Cluster...')
        task_url = 'https://'+self.hostname+'/v1/tasks/' + response['id']
        print('Create cluster ended with status: ' + self.utils.poll_on_id(task_url,True))


if __name__ == "__main__":
    CreateCluster().create_cluster()


