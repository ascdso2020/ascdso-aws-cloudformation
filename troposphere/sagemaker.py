# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class ResourceSpec(AWSProperty):
    """
    `ResourceSpec <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html>`__
    """

    props: PropsDictType = {
        "InstanceType": (str, False),
        "SageMakerImageArn": (str, False),
        "SageMakerImageVersionArn": (str, False),
    }


class App(AWSObject):
    """
    `App <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html>`__
    """

    resource_type = "AWS::SageMaker::App"

    props: PropsDictType = {
        "AppName": (str, True),
        "AppType": (str, True),
        "DomainId": (str, True),
        "ResourceSpec": (ResourceSpec, False),
        "Tags": (Tags, False),
        "UserProfileName": (str, True),
    }


class FileSystemConfig(AWSProperty):
    """
    `FileSystemConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html>`__
    """

    props: PropsDictType = {
        "DefaultGid": (integer, False),
        "DefaultUid": (integer, False),
        "MountPath": (str, False),
    }


class KernelSpec(AWSProperty):
    """
    `KernelSpec <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html>`__
    """

    props: PropsDictType = {
        "DisplayName": (str, False),
        "Name": (str, True),
    }


class KernelGatewayImageConfig(AWSProperty):
    """
    `KernelGatewayImageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html>`__
    """

    props: PropsDictType = {
        "FileSystemConfig": (FileSystemConfig, False),
        "KernelSpecs": ([KernelSpec], True),
    }


class AppImageConfig(AWSObject):
    """
    `AppImageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html>`__
    """

    resource_type = "AWS::SageMaker::AppImageConfig"

    props: PropsDictType = {
        "AppImageConfigName": (str, True),
        "KernelGatewayImageConfig": (KernelGatewayImageConfig, False),
        "Tags": (Tags, False),
    }


class GitConfig(AWSProperty):
    """
    `GitConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html>`__
    """

    props: PropsDictType = {
        "Branch": (str, False),
        "RepositoryUrl": (str, True),
        "SecretArn": (str, False),
    }


class CodeRepository(AWSObject):
    """
    `CodeRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html>`__
    """

    resource_type = "AWS::SageMaker::CodeRepository"

    props: PropsDictType = {
        "CodeRepositoryName": (str, False),
        "GitConfig": (GitConfig, True),
        "Tags": (Tags, False),
    }


class DataQualityAppSpecification(AWSProperty):
    """
    `DataQualityAppSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html>`__
    """

    props: PropsDictType = {
        "ContainerArguments": ([str], False),
        "ContainerEntrypoint": ([str], False),
        "Environment": (dict, False),
        "ImageUri": (str, True),
        "PostAnalyticsProcessorSourceUri": (str, False),
        "RecordPreprocessorSourceUri": (str, False),
    }


class ConstraintsResource(AWSProperty):
    """
    `ConstraintsResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html>`__
    """

    props: PropsDictType = {
        "S3Uri": (str, False),
    }


class StatisticsResource(AWSProperty):
    """
    `StatisticsResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html>`__
    """

    props: PropsDictType = {
        "S3Uri": (str, False),
    }


class DataQualityBaselineConfig(AWSProperty):
    """
    `DataQualityBaselineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html>`__
    """

    props: PropsDictType = {
        "BaseliningJobName": (str, False),
        "ConstraintsResource": (ConstraintsResource, False),
        "StatisticsResource": (StatisticsResource, False),
    }


class EndpointInput(AWSProperty):
    """
    `EndpointInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html>`__
    """

    props: PropsDictType = {
        "EndpointName": (str, True),
        "LocalPath": (str, True),
        "S3DataDistributionType": (str, False),
        "S3InputMode": (str, False),
    }


class DataQualityJobInput(AWSProperty):
    """
    `DataQualityJobInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html>`__
    """

    props: PropsDictType = {
        "EndpointInput": (EndpointInput, True),
    }


class S3Output(AWSProperty):
    """
    `S3Output <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html>`__
    """

    props: PropsDictType = {
        "LocalPath": (str, True),
        "S3UploadMode": (str, False),
        "S3Uri": (str, True),
    }


class MonitoringOutput(AWSProperty):
    """
    `MonitoringOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html>`__
    """

    props: PropsDictType = {
        "S3Output": (S3Output, True),
    }


class MonitoringOutputConfig(AWSProperty):
    """
    `MonitoringOutputConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "MonitoringOutputs": ([MonitoringOutput], True),
    }


class ClusterConfig(AWSProperty):
    """
    `ClusterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html>`__
    """

    props: PropsDictType = {
        "InstanceCount": (integer, True),
        "InstanceType": (str, True),
        "VolumeKmsKeyId": (str, False),
        "VolumeSizeInGB": (integer, True),
    }


class MonitoringResources(AWSProperty):
    """
    `MonitoringResources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html>`__
    """

    props: PropsDictType = {
        "ClusterConfig": (ClusterConfig, True),
    }


class VpcConfig(AWSProperty):
    """
    `VpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "Subnets": ([str], True),
    }


class NetworkConfig(AWSProperty):
    """
    `NetworkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html>`__
    """

    props: PropsDictType = {
        "EnableInterContainerTrafficEncryption": (boolean, False),
        "EnableNetworkIsolation": (boolean, False),
        "VpcConfig": (VpcConfig, False),
    }


class StoppingCondition(AWSProperty):
    """
    `StoppingCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html>`__
    """

    props: PropsDictType = {
        "MaxRuntimeInSeconds": (integer, True),
    }


class DataQualityJobDefinition(AWSObject):
    """
    `DataQualityJobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html>`__
    """

    resource_type = "AWS::SageMaker::DataQualityJobDefinition"

    props: PropsDictType = {
        "DataQualityAppSpecification": (DataQualityAppSpecification, True),
        "DataQualityBaselineConfig": (DataQualityBaselineConfig, False),
        "DataQualityJobInput": (DataQualityJobInput, True),
        "DataQualityJobOutputConfig": (MonitoringOutputConfig, True),
        "JobDefinitionName": (str, False),
        "JobResources": (MonitoringResources, True),
        "NetworkConfig": (NetworkConfig, False),
        "RoleArn": (str, True),
        "StoppingCondition": (StoppingCondition, False),
        "Tags": (Tags, False),
    }


class DeviceProperty(AWSProperty):
    """
    `DeviceProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "DeviceName": (str, True),
        "IotThingName": (str, False),
    }


class Device(AWSObject):
    """
    `Device <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html>`__
    """

    resource_type = "AWS::SageMaker::Device"

    props: PropsDictType = {
        "Device": (DeviceProperty, False),
        "DeviceFleetName": (str, True),
        "Tags": (Tags, False),
    }


class EdgeOutputConfig(AWSProperty):
    """
    `EdgeOutputConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "S3OutputLocation": (str, True),
    }


class DeviceFleet(AWSObject):
    """
    `DeviceFleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html>`__
    """

    resource_type = "AWS::SageMaker::DeviceFleet"

    props: PropsDictType = {
        "Description": (str, False),
        "DeviceFleetName": (str, True),
        "OutputConfig": (EdgeOutputConfig, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class JupyterServerAppSettings(AWSProperty):
    """
    `JupyterServerAppSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html>`__
    """

    props: PropsDictType = {
        "DefaultResourceSpec": (ResourceSpec, False),
    }


class CustomImage(AWSProperty):
    """
    `CustomImage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html>`__
    """

    props: PropsDictType = {
        "AppImageConfigName": (str, True),
        "ImageName": (str, True),
        "ImageVersionNumber": (integer, False),
    }


class KernelGatewayAppSettings(AWSProperty):
    """
    `KernelGatewayAppSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html>`__
    """

    props: PropsDictType = {
        "CustomImages": ([CustomImage], False),
        "DefaultResourceSpec": (ResourceSpec, False),
    }


class SharingSettings(AWSProperty):
    """
    `SharingSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html>`__
    """

    props: PropsDictType = {
        "NotebookOutputOption": (str, False),
        "S3KmsKeyId": (str, False),
        "S3OutputPath": (str, False),
    }


class UserSettings(AWSProperty):
    """
    `UserSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html>`__
    """

    props: PropsDictType = {
        "ExecutionRole": (str, False),
        "JupyterServerAppSettings": (JupyterServerAppSettings, False),
        "KernelGatewayAppSettings": (KernelGatewayAppSettings, False),
        "SecurityGroups": ([str], False),
        "SharingSettings": (SharingSettings, False),
    }


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html>`__
    """

    resource_type = "AWS::SageMaker::Domain"

    props: PropsDictType = {
        "AppNetworkAccessType": (str, False),
        "AuthMode": (str, True),
        "DefaultUserSettings": (UserSettings, True),
        "DomainName": (str, True),
        "KmsKeyId": (str, False),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class Alarm(AWSProperty):
    """
    `Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html>`__
    """

    props: PropsDictType = {
        "AlarmName": (str, True),
    }


class AutoRollbackConfig(AWSProperty):
    """
    `AutoRollbackConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html>`__
    """

    props: PropsDictType = {
        "Alarms": ([Alarm], True),
    }


class CapacitySize(AWSProperty):
    """
    `CapacitySize <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (integer, True),
    }


class TrafficRoutingConfig(AWSProperty):
    """
    `TrafficRoutingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html>`__
    """

    props: PropsDictType = {
        "CanarySize": (CapacitySize, False),
        "LinearStepSize": (CapacitySize, False),
        "Type": (str, True),
        "WaitIntervalInSeconds": (integer, False),
    }


class BlueGreenUpdatePolicy(AWSProperty):
    """
    `BlueGreenUpdatePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html>`__
    """

    props: PropsDictType = {
        "MaximumExecutionTimeoutInSeconds": (integer, False),
        "TerminationWaitInSeconds": (integer, False),
        "TrafficRoutingConfiguration": (TrafficRoutingConfig, True),
    }


class DeploymentConfig(AWSProperty):
    """
    `DeploymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html>`__
    """

    props: PropsDictType = {
        "AutoRollbackConfiguration": (AutoRollbackConfig, False),
        "BlueGreenUpdatePolicy": (BlueGreenUpdatePolicy, True),
    }


class VariantProperty(AWSProperty):
    """
    `VariantProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html>`__
    """

    props: PropsDictType = {
        "VariantPropertyType": (str, False),
    }


class Endpoint(AWSObject):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html>`__
    """

    resource_type = "AWS::SageMaker::Endpoint"

    props: PropsDictType = {
        "DeploymentConfig": (DeploymentConfig, False),
        "EndpointConfigName": (str, True),
        "EndpointName": (str, False),
        "ExcludeRetainedVariantProperties": ([VariantProperty], False),
        "RetainAllVariantProperties": (boolean, False),
        "RetainDeploymentConfig": (boolean, False),
        "Tags": (Tags, False),
    }


class AsyncInferenceClientConfig(AWSProperty):
    """
    `AsyncInferenceClientConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html>`__
    """

    props: PropsDictType = {
        "MaxConcurrentInvocationsPerInstance": (integer, False),
    }


class AsyncInferenceNotificationConfig(AWSProperty):
    """
    `AsyncInferenceNotificationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html>`__
    """

    props: PropsDictType = {
        "ErrorTopic": (str, False),
        "SuccessTopic": (str, False),
    }


class AsyncInferenceOutputConfig(AWSProperty):
    """
    `AsyncInferenceOutputConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "NotificationConfig": (AsyncInferenceNotificationConfig, False),
        "S3OutputPath": (str, True),
    }


class AsyncInferenceConfig(AWSProperty):
    """
    `AsyncInferenceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html>`__
    """

    props: PropsDictType = {
        "ClientConfig": (AsyncInferenceClientConfig, False),
        "OutputConfig": (AsyncInferenceOutputConfig, True),
    }


class CaptureContentTypeHeader(AWSProperty):
    """
    `CaptureContentTypeHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html>`__
    """

    props: PropsDictType = {
        "CsvContentTypes": ([str], False),
        "JsonContentTypes": ([str], False),
    }


class CaptureOption(AWSProperty):
    """
    `CaptureOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html>`__
    """

    props: PropsDictType = {
        "CaptureMode": (str, True),
    }


class DataCaptureConfig(AWSProperty):
    """
    `DataCaptureConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html>`__
    """

    props: PropsDictType = {
        "CaptureContentTypeHeader": (CaptureContentTypeHeader, False),
        "CaptureOptions": ([CaptureOption], True),
        "DestinationS3Uri": (str, True),
        "EnableCapture": (boolean, False),
        "InitialSamplingPercentage": (integer, True),
        "KmsKeyId": (str, False),
    }


class ServerlessConfig(AWSProperty):
    """
    `ServerlessConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html>`__
    """

    props: PropsDictType = {
        "MaxConcurrency": (integer, True),
        "MemorySizeInMB": (integer, True),
    }


class ProductionVariant(AWSProperty):
    """
    `ProductionVariant <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html>`__
    """

    props: PropsDictType = {
        "AcceleratorType": (str, False),
        "InitialInstanceCount": (integer, False),
        "InitialVariantWeight": (double, True),
        "InstanceType": (str, False),
        "ModelName": (str, True),
        "ServerlessConfig": (ServerlessConfig, False),
        "VariantName": (str, True),
    }


class EndpointConfig(AWSObject):
    """
    `EndpointConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html>`__
    """

    resource_type = "AWS::SageMaker::EndpointConfig"

    props: PropsDictType = {
        "AsyncInferenceConfig": (AsyncInferenceConfig, False),
        "DataCaptureConfig": (DataCaptureConfig, False),
        "EndpointConfigName": (str, False),
        "KmsKeyId": (str, False),
        "ProductionVariants": ([ProductionVariant], True),
        "Tags": (Tags, False),
    }


class FeatureDefinition(AWSProperty):
    """
    `FeatureDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html>`__
    """

    props: PropsDictType = {
        "FeatureName": (str, True),
        "FeatureType": (str, True),
    }


class FeatureGroup(AWSObject):
    """
    `FeatureGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html>`__
    """

    resource_type = "AWS::SageMaker::FeatureGroup"

    props: PropsDictType = {
        "Description": (str, False),
        "EventTimeFeatureName": (str, True),
        "FeatureDefinitions": ([FeatureDefinition], True),
        "FeatureGroupName": (str, True),
        "OfflineStoreConfig": (dict, False),
        "OnlineStoreConfig": (dict, False),
        "RecordIdentifierFeatureName": (str, True),
        "RoleArn": (str, False),
        "Tags": (Tags, False),
    }


class Image(AWSObject):
    """
    `Image <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html>`__
    """

    resource_type = "AWS::SageMaker::Image"

    props: PropsDictType = {
        "ImageDescription": (str, False),
        "ImageDisplayName": (str, False),
        "ImageName": (str, True),
        "ImageRoleArn": (str, True),
        "Tags": (Tags, False),
    }


class ImageVersion(AWSObject):
    """
    `ImageVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html>`__
    """

    resource_type = "AWS::SageMaker::ImageVersion"

    props: PropsDictType = {
        "BaseImage": (str, True),
        "ImageName": (str, True),
    }


class RepositoryAuthConfig(AWSProperty):
    """
    `RepositoryAuthConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html>`__
    """

    props: PropsDictType = {
        "RepositoryCredentialsProviderArn": (str, True),
    }


class ImageConfig(AWSProperty):
    """
    `ImageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html>`__
    """

    props: PropsDictType = {
        "RepositoryAccessMode": (str, True),
        "RepositoryAuthConfig": (RepositoryAuthConfig, False),
    }


class MultiModelConfig(AWSProperty):
    """
    `MultiModelConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html>`__
    """

    props: PropsDictType = {
        "ModelCacheSetting": (str, False),
    }


class ContainerDefinition(AWSProperty):
    """
    `ContainerDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html>`__
    """

    props: PropsDictType = {
        "ContainerHostname": (str, False),
        "Environment": (dict, False),
        "Image": (str, False),
        "ImageConfig": (ImageConfig, False),
        "InferenceSpecificationName": (str, False),
        "Mode": (str, False),
        "ModelDataUrl": (str, False),
        "ModelPackageName": (str, False),
        "MultiModelConfig": (MultiModelConfig, False),
    }


class InferenceExecutionConfig(AWSProperty):
    """
    `InferenceExecutionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, True),
    }


class Model(AWSObject):
    """
    `Model <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html>`__
    """

    resource_type = "AWS::SageMaker::Model"

    props: PropsDictType = {
        "Containers": ([ContainerDefinition], False),
        "EnableNetworkIsolation": (boolean, False),
        "ExecutionRoleArn": (str, True),
        "InferenceExecutionConfig": (InferenceExecutionConfig, False),
        "ModelName": (str, False),
        "PrimaryContainer": (ContainerDefinition, False),
        "Tags": (Tags, False),
        "VpcConfig": (VpcConfig, False),
    }


class ModelBiasAppSpecification(AWSProperty):
    """
    `ModelBiasAppSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html>`__
    """

    props: PropsDictType = {
        "ConfigUri": (str, True),
        "Environment": (dict, False),
        "ImageUri": (str, True),
    }


class ModelBiasBaselineConfig(AWSProperty):
    """
    `ModelBiasBaselineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html>`__
    """

    props: PropsDictType = {
        "BaseliningJobName": (str, False),
        "ConstraintsResource": (ConstraintsResource, False),
    }


class MonitoringGroundTruthS3Input(AWSProperty):
    """
    `MonitoringGroundTruthS3Input <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html>`__
    """

    props: PropsDictType = {
        "S3Uri": (str, True),
    }


class ModelBiasJobInput(AWSProperty):
    """
    `ModelBiasJobInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html>`__
    """

    props: PropsDictType = {
        "EndpointInput": (EndpointInput, True),
        "GroundTruthS3Input": (MonitoringGroundTruthS3Input, True),
    }


class ModelBiasJobDefinition(AWSObject):
    """
    `ModelBiasJobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html>`__
    """

    resource_type = "AWS::SageMaker::ModelBiasJobDefinition"

    props: PropsDictType = {
        "JobDefinitionName": (str, False),
        "JobResources": (MonitoringResources, True),
        "ModelBiasAppSpecification": (ModelBiasAppSpecification, True),
        "ModelBiasBaselineConfig": (ModelBiasBaselineConfig, False),
        "ModelBiasJobInput": (ModelBiasJobInput, True),
        "ModelBiasJobOutputConfig": (MonitoringOutputConfig, True),
        "NetworkConfig": (NetworkConfig, False),
        "RoleArn": (str, True),
        "StoppingCondition": (StoppingCondition, False),
        "Tags": (Tags, False),
    }


class ModelExplainabilityAppSpecification(AWSProperty):
    """
    `ModelExplainabilityAppSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html>`__
    """

    props: PropsDictType = {
        "ConfigUri": (str, True),
        "Environment": (dict, False),
        "ImageUri": (str, True),
    }


class ModelExplainabilityBaselineConfig(AWSProperty):
    """
    `ModelExplainabilityBaselineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html>`__
    """

    props: PropsDictType = {
        "BaseliningJobName": (str, False),
        "ConstraintsResource": (ConstraintsResource, False),
    }


class ModelExplainabilityJobInput(AWSProperty):
    """
    `ModelExplainabilityJobInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html>`__
    """

    props: PropsDictType = {
        "EndpointInput": (EndpointInput, True),
    }


class ModelExplainabilityJobDefinition(AWSObject):
    """
    `ModelExplainabilityJobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html>`__
    """

    resource_type = "AWS::SageMaker::ModelExplainabilityJobDefinition"

    props: PropsDictType = {
        "JobDefinitionName": (str, False),
        "JobResources": (MonitoringResources, True),
        "ModelExplainabilityAppSpecification": (
            ModelExplainabilityAppSpecification,
            True,
        ),
        "ModelExplainabilityBaselineConfig": (ModelExplainabilityBaselineConfig, False),
        "ModelExplainabilityJobInput": (ModelExplainabilityJobInput, True),
        "ModelExplainabilityJobOutputConfig": (MonitoringOutputConfig, True),
        "NetworkConfig": (NetworkConfig, False),
        "RoleArn": (str, True),
        "StoppingCondition": (StoppingCondition, False),
        "Tags": (Tags, False),
    }


class ModelPackageGroup(AWSObject):
    """
    `ModelPackageGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html>`__
    """

    resource_type = "AWS::SageMaker::ModelPackageGroup"

    props: PropsDictType = {
        "ModelPackageGroupDescription": (str, False),
        "ModelPackageGroupName": (str, True),
        "ModelPackageGroupPolicy": (dict, False),
        "Tags": (Tags, False),
    }


class ModelQualityAppSpecification(AWSProperty):
    """
    `ModelQualityAppSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html>`__
    """

    props: PropsDictType = {
        "ContainerArguments": ([str], False),
        "ContainerEntrypoint": ([str], False),
        "Environment": (dict, False),
        "ImageUri": (str, True),
        "PostAnalyticsProcessorSourceUri": (str, False),
        "ProblemType": (str, True),
        "RecordPreprocessorSourceUri": (str, False),
    }


class ModelQualityBaselineConfig(AWSProperty):
    """
    `ModelQualityBaselineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html>`__
    """

    props: PropsDictType = {
        "BaseliningJobName": (str, False),
        "ConstraintsResource": (ConstraintsResource, False),
    }


class ModelQualityJobInput(AWSProperty):
    """
    `ModelQualityJobInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html>`__
    """

    props: PropsDictType = {
        "EndpointInput": (EndpointInput, True),
        "GroundTruthS3Input": (MonitoringGroundTruthS3Input, True),
    }


class ModelQualityJobDefinition(AWSObject):
    """
    `ModelQualityJobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html>`__
    """

    resource_type = "AWS::SageMaker::ModelQualityJobDefinition"

    props: PropsDictType = {
        "JobDefinitionName": (str, False),
        "JobResources": (MonitoringResources, True),
        "ModelQualityAppSpecification": (ModelQualityAppSpecification, True),
        "ModelQualityBaselineConfig": (ModelQualityBaselineConfig, False),
        "ModelQualityJobInput": (ModelQualityJobInput, True),
        "ModelQualityJobOutputConfig": (MonitoringOutputConfig, True),
        "NetworkConfig": (NetworkConfig, False),
        "RoleArn": (str, True),
        "StoppingCondition": (StoppingCondition, False),
        "Tags": (Tags, False),
    }


class MonitoringExecutionSummary(AWSProperty):
    """
    `MonitoringExecutionSummary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html>`__
    """

    props: PropsDictType = {
        "CreationTime": (str, True),
        "EndpointName": (str, False),
        "FailureReason": (str, False),
        "LastModifiedTime": (str, True),
        "MonitoringExecutionStatus": (str, True),
        "MonitoringScheduleName": (str, True),
        "ProcessingJobArn": (str, False),
        "ScheduledTime": (str, True),
    }


class BaselineConfig(AWSProperty):
    """
    `BaselineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html>`__
    """

    props: PropsDictType = {
        "ConstraintsResource": (ConstraintsResource, False),
        "StatisticsResource": (StatisticsResource, False),
    }


class MonitoringAppSpecification(AWSProperty):
    """
    `MonitoringAppSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html>`__
    """

    props: PropsDictType = {
        "ContainerArguments": ([str], False),
        "ContainerEntrypoint": ([str], False),
        "ImageUri": (str, True),
        "PostAnalyticsProcessorSourceUri": (str, False),
        "RecordPreprocessorSourceUri": (str, False),
    }


class MonitoringInput(AWSProperty):
    """
    `MonitoringInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html>`__
    """

    props: PropsDictType = {
        "EndpointInput": (EndpointInput, True),
    }


class MonitoringJobDefinition(AWSProperty):
    """
    `MonitoringJobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html>`__
    """

    props: PropsDictType = {
        "BaselineConfig": (BaselineConfig, False),
        "Environment": (dict, False),
        "MonitoringAppSpecification": (MonitoringAppSpecification, True),
        "MonitoringInputs": ([MonitoringInput], True),
        "MonitoringOutputConfig": (MonitoringOutputConfig, True),
        "MonitoringResources": (MonitoringResources, True),
        "NetworkConfig": (NetworkConfig, False),
        "RoleArn": (str, True),
        "StoppingCondition": (StoppingCondition, False),
    }


class ScheduleConfig(AWSProperty):
    """
    `ScheduleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html>`__
    """

    props: PropsDictType = {
        "ScheduleExpression": (str, True),
    }


class MonitoringScheduleConfig(AWSProperty):
    """
    `MonitoringScheduleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html>`__
    """

    props: PropsDictType = {
        "MonitoringJobDefinition": (MonitoringJobDefinition, False),
        "MonitoringJobDefinitionName": (str, False),
        "MonitoringType": (str, False),
        "ScheduleConfig": (ScheduleConfig, False),
    }


class MonitoringSchedule(AWSObject):
    """
    `MonitoringSchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html>`__
    """

    resource_type = "AWS::SageMaker::MonitoringSchedule"

    props: PropsDictType = {
        "EndpointName": (str, False),
        "FailureReason": (str, False),
        "LastMonitoringExecutionSummary": (MonitoringExecutionSummary, False),
        "MonitoringScheduleConfig": (MonitoringScheduleConfig, True),
        "MonitoringScheduleName": (str, True),
        "MonitoringScheduleStatus": (str, False),
        "Tags": (Tags, False),
    }


class NotebookInstance(AWSObject):
    """
    `NotebookInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html>`__
    """

    resource_type = "AWS::SageMaker::NotebookInstance"

    props: PropsDictType = {
        "AcceleratorTypes": ([str], False),
        "AdditionalCodeRepositories": ([str], False),
        "DefaultCodeRepository": (str, False),
        "DirectInternetAccess": (str, False),
        "InstanceType": (str, True),
        "KmsKeyId": (str, False),
        "LifecycleConfigName": (str, False),
        "NotebookInstanceName": (str, False),
        "PlatformIdentifier": (str, False),
        "RoleArn": (str, True),
        "RootAccess": (str, False),
        "SecurityGroupIds": ([str], False),
        "SubnetId": (str, False),
        "Tags": (Tags, False),
        "VolumeSizeInGB": (integer, False),
    }


class NotebookInstanceLifecycleHook(AWSProperty):
    """
    `NotebookInstanceLifecycleHook <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html>`__
    """

    props: PropsDictType = {
        "Content": (str, False),
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    """
    `NotebookInstanceLifecycleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html>`__
    """

    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props: PropsDictType = {
        "NotebookInstanceLifecycleConfigName": (str, False),
        "OnCreate": ([NotebookInstanceLifecycleHook], False),
        "OnStart": ([NotebookInstanceLifecycleHook], False),
    }


class Pipeline(AWSObject):
    """
    `Pipeline <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html>`__
    """

    resource_type = "AWS::SageMaker::Pipeline"

    props: PropsDictType = {
        "ParallelismConfiguration": (dict, False),
        "PipelineDefinition": (dict, True),
        "PipelineDescription": (str, False),
        "PipelineDisplayName": (str, False),
        "PipelineName": (str, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html>`__
    """

    resource_type = "AWS::SageMaker::Project"

    props: PropsDictType = {
        "ProjectDescription": (str, False),
        "ProjectName": (str, True),
        "ServiceCatalogProvisioningDetails": (dict, True),
        "Tags": (Tags, False),
    }


class UserProfile(AWSObject):
    """
    `UserProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html>`__
    """

    resource_type = "AWS::SageMaker::UserProfile"

    props: PropsDictType = {
        "DomainId": (str, True),
        "SingleSignOnUserIdentifier": (str, False),
        "SingleSignOnUserValue": (str, False),
        "Tags": (Tags, False),
        "UserProfileName": (str, True),
        "UserSettings": (UserSettings, False),
    }


class CognitoMemberDefinition(AWSProperty):
    """
    `CognitoMemberDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html>`__
    """

    props: PropsDictType = {
        "CognitoClientId": (str, True),
        "CognitoUserGroup": (str, True),
        "CognitoUserPool": (str, True),
    }


class MemberDefinition(AWSProperty):
    """
    `MemberDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html>`__
    """

    props: PropsDictType = {
        "CognitoMemberDefinition": (CognitoMemberDefinition, True),
    }


class NotificationConfiguration(AWSProperty):
    """
    `NotificationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html>`__
    """

    props: PropsDictType = {
        "NotificationTopicArn": (str, True),
    }


class Workteam(AWSObject):
    """
    `Workteam <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html>`__
    """

    resource_type = "AWS::SageMaker::Workteam"

    props: PropsDictType = {
        "Description": (str, False),
        "MemberDefinitions": ([MemberDefinition], False),
        "NotificationConfiguration": (NotificationConfiguration, False),
        "Tags": (Tags, False),
        "WorkteamName": (str, False),
    }
