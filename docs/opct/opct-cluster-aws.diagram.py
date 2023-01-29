from diagrams import Cluster, Diagram
from diagrams.aws.compute import (
    EC2, EC2Instances
)
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("OCP/OKD Cluster", show=False, filename="./opct-ocp-cluster-aws"):
    dnsApiExt = Route53("api.<cluster>.<domain>")
    dnsApsExt = Route53("*.apps.<cluster>.<domain>")

    with Cluster("VPC/Network"):

        with Cluster("VPC Public subnets"):
            lbe_api = ELB("API-Ext")
            lbe_apps = ELB("Apps-Ext")
        
        with Cluster("VPC Private subnets"):
            lbi_api = ELB("API-Int")
            dnsApiInt = Route53("api-int.<cluster>.<domain>")
            with Cluster("Control Plane Pool"):
                # cp_group = [EC2("control-plane-01"),
                #             EC2("control-plane-02"),
                #             EC2("control-plane-03")]
                cp_group = [EC2Instances("master-0{1,2,3}")]

            with Cluster("Compute Pool"):
                # wk_group = [EC2("compute-01"),
                #             EC2("compute-02"),
                #             EC2("compute-03")]
                wk_group = [EC2Instances("compute-0{1,2,3}")]

    # with Cluster("DB Cluster"):
    #     db_primary = RDS("userdb")
    #     db_primary - [RDS("userdb ro")]

    # memcached = ElastiCache("memcached")

    dnsApiExt >> lbe_api >> cp_group
    dnsApiInt >> lbi_api >> cp_group
    cp_group >> dnsApiInt >> lbi_api
    wk_group >> dnsApiInt >> lbi_api
    dnsApsExt >> lbe_apps >> wk_group
    
    # cp_group >> db_primary
    # cp_group >> memcached
