from diagrams import Cluster, Diagram

from diagrams.k8s.compute import (
    Pod, Job
)
from diagrams.k8s.network import Service
from diagrams.k8s.group import NS
from diagrams.oci.compute import Container

from diagrams.aws.general import InternetAlt2

from diagrams.custom import Custom
from urllib.request import urlretrieve

from diagrams.k8s.infra import ( Node )
from diagrams.k8s.controlplane import APIServer

from diagrams.generic.os import RedHat

with Diagram("OCP/OKD Cluster", show=False, filename="./opct-plugin"):

    openshift_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/OpenShift-LogoType.svg"
    openshift_icon = "openshift.png"
    urlretrieve(openshift_url, openshift_icon)

    k8s_url = "https://cncf-branding.netlify.app/img/projects/kubernetes/stacked/color/kubernetes-stacked-color.png"
    k8s_icon = "k8s.png"
    urlretrieve(k8s_url, k8s_icon)


    with Cluster("VPC/Network"):

        with Cluster("VPC Public subnets"):
            internet = InternetAlt2("gateway")

        with Cluster("VPC Private subnets"):
            with Cluster("OPCT Dedicated Node"):
                ded_node = [Node("compute-04")]

                ded_node >> internet

        with Cluster("OpenShift Container Platform"):

            with Cluster("e2e tests"):
                openshift = Custom("OpenShift", openshift_icon)
                k8s = Custom("Kubernetes", k8s_icon)    

            with Cluster("Validation Environment"):
                ns = NS("openshift-provider-certification")
                ded_node >> ns
                sb_pod = Pod("sonobuoy")
                sb_svc = Service("aggregator")

                with Cluster("Plugin"):
                    plugin = Job("Plugin-<NAME>")
                    cnt_worker = Container("worker")
                    cnt_plugin = Container("plugin")
                    cnt_progress = Container("progress")
                    
                    cnt_plugin >> [cnt_progress, cnt_worker]
                    [cnt_progress, cnt_worker] >> sb_svc
                
                sb_svc >> sb_pod >> plugin

    cnt_plugin >> [openshift, k8s]
