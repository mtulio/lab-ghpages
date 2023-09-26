from diagrams import Cluster, Diagram, Edge

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

    try:
        k8s_url = "https://cncf-branding.netlify.app/img/projects/kubernetes/stacked/color/kubernetes-stacked-color.png"
        k8s_icon = "k8s.png"
        urlretrieve(k8s_url, k8s_icon)
    except Exception as e:
        print(f"ERROR unable to download k8s icon in the URL {k8s_url}")
        #raise e


    with Cluster("VPC/Network"):

        with Cluster("VPC Public subnets"):
            internet = InternetAlt2("gateway")

        with Cluster("VPC Private subnets"):
            with Cluster("OPCT Dedicated Node"):
                ded_node = [Node("compute-04")]
                ded_node >> internet

        with Cluster("OpenShift Container Platform"):

            with Cluster("e2e tests"):
                openshift = Custom("", openshift_icon)
                k8s = Custom("", k8s_icon)
                api = APIServer("Kube-apiserver")

            with Cluster("Validation Environment"):
                ns = NS("openshift-provider-certification")
                ded_node << ns
                sb_pod = Pod("sonobuoy")
                sb_svc = Service("aggregator")
                plugin = Job("Plugin-<NAME>")
                with Cluster("Plugin"):
                    
                    cnt_worker = Container("worker")
                    cnt_plugin = Container("plugin")
                    cnt_progress = Container("progress")
                    
                    cnt_plugin >> Edge(label="stdout pipe", color="firebrick", style="dashed") >> cnt_progress
                    cnt_plugin >> Edge(label="", color="firebrick", style="bold") >> cnt_worker
                    [cnt_progress, cnt_worker] >> sb_svc
                
                #plugin - [cnt_plugin, cnt_progress, cnt_worker]
                plugin - cnt_plugin
                sb_svc >> sb_pod >> plugin

    cnt_plugin >> Edge(label="run e2e", color="firebrick", style="bold") >> api
    api - [openshift, k8s]
