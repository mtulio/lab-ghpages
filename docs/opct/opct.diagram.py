from diagrams import Cluster, Diagram

from diagrams.k8s.compute import Deployment, Pod, ReplicaSet, Job
from diagrams.k8s.network import Ingress, Service

from diagrams.k8s.infra import ( Node, Master )

from diagrams.generic.os import RedHat

with Diagram("OCP/OKD Cluster", show=False, filename="./opct"):
    
    with Cluster("OpenShift Container Platform"):
        # k8s = Custom("", k8s_icon)
        with Cluster("OPCT Dedicated Node"):
            ded_node = [Node("compute-04")]

        # ns = NS("opct")
        with Cluster("Namespace=openshift-provider-certification"):
            sb_pod = Pod("sonobuoy")
            sb_svc = Service("aggregator")

            with Cluster("Plugins"):
                plugins_group = [
                    Job("10-kube-conformance"),
                    Job("10-ocp-conformance"),
                    Job("10-ocp-upgrade"),
                    Job("10-artifacts-collector")]

    # ded_node >> [sb_pod]
    sb_pod >> plugins_group >> sb_svc
    sb_svc >> sb_pod
    
