![images/banner.png](images/banner.png)

# Innovate AI/ML EMEA 2021

### OPS4 - Build your ML platforms using open source technology

### Resources

During this presentation I talked about a few resources to help you get started and configure your Apache Airflow environments. Here are links to these resources.

* [Airflow workshop from Delivery Hero](https://github.com/deliveryhero/pyconde2019-airflow-ml-workshop)- Check out this great starting workshop that was put together by Delivery Hero at PyConde 2019.
* [Running Apache Airflow locally via Docker](https://aws-oss.beachgeek.co.uk/3g) - this is the Docker compose file I showed and started. It mounts a local volume (dags) that you can use to upload DAGs for development.
* [Apache Airflow main page](https://airflow.apache.org/)
* [Machine Learning in Production using Apache Airflow](https://aws-oss.beachgeek.co.uk/2g)

---
### Amazon Managed Workflows for Apache Airflow resources

Installing Amazon Managed Workflows for Apache Airflow via Cloudformation templates
Setting up permissions for developers
Setting up permissions for your workers
A simple development workflow for managing your Apache Airflow DAGs

**Integration with Amazon Elastic Map Reduce for big data workloads**

* [Running PySpark Applications on Amazon EMR](https://aws-oss.beachgeek.co.uk/18)
* [Running Spark Jobs on Amazon EMR with Apache Airflow](https://aws-oss.beachgeek.co.uk/19)
* [Building complex workflows with Amazon MWAA, AWS Step Functions, AWS Glue, and Amazon EMR](https://aws-oss.beachgeek.co.uk/1s)

**Integration with Amazon SageMaker for training and hyper-parameter tuning**

* [Amazon Sagemaker Workshop / Airflow Integration](https://aws-oss.beachgeek.co.uk/2h) workshop - https://www.sagemakerworkshop.com/airflow/](https://aws-oss.beachgeek.co.uk/2h) - reproduce the Amazon SageMaker DAG yourself.

**Integration with Amazon Personalize**

* [Managed Workflows for Apache Workflow and Amazon Personalise](https://aws-oss.beachgeek.co.uk/2e) - Great blog post and source code from AWS Community Builder, Yi Ai.

**CloudFormation templates**

You will find a number of scripts to help you automate your installation and configuration. You can find them in this folder [cf](cf)

You need to setup and deploy the networking first before deploying the Managed Workflows for Apache Airflow. You can combine these if you want but will need to change the template to incorporate how you incorporate the parameters.

You can run the templates via the AWS Cloudformation gui and then enter the parameters as needed. Observations on usage:

* for the S3 bucket, make sure it is prefixed "airflow-"
* when selecting the subnets, make sure you are using the private subnets not the public ones
* ensure the region you are deploying currently has Managed Workflows for Apache Airflow

You can modify the template with your own defaults. These are starter templates that can be improved -for example, asking for more user definable setting such as Worker instance sizes or logging information.

There are two scripts provided to show you how these settings look: a public facing and a private instance.

**AWS CLI and Parameter files**

To run the deployment via the command  line, use the following parameter file changing the values based on the outputs of the networking script.

```
[
    {
      "ParameterKey": "s3BucketName",
      "ParameterValue": "airflow-xxxx"
    }, 
    {
      "ParameterKey": "subnetIds",
      "ParameterValue": "{privatesubnet1-id},{privatesubnet2-id}"
    },
    {
        "ParameterKey": "vpcId",
        "ParameterValue": "{vpc-id}"
      }
  ]
```

You can then use the following commands to submit to AWS Cloudformation and then monitor via cli/console.

```
aws cloudformation create-stack --stack-name {your-unique-stack-name} --template-body file://mwaa-vpc-cfn.yaml
```
```
aws cloudformation create-stack --stack-name {your-unique-stack-name} --template-body file://install-mwaa-public.yaml --parameters file://mwaa-cfn-parameters.json --capabilities CAPABILITY_IAM --region={region}
```