# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double
from .validators.appsync import resolver_kind_validator


class ApiCache(AWSObject):
    """
    `ApiCache <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html>`__
    """

    resource_type = "AWS::AppSync::ApiCache"

    props: PropsDictType = {
        "ApiCachingBehavior": (str, True),
        "ApiId": (str, True),
        "AtRestEncryptionEnabled": (boolean, False),
        "TransitEncryptionEnabled": (boolean, False),
        "Ttl": (double, True),
        "Type": (str, True),
    }


class ApiKey(AWSObject):
    """
    `ApiKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html>`__
    """

    resource_type = "AWS::AppSync::ApiKey"

    props: PropsDictType = {
        "ApiId": (str, True),
        "ApiKeyId": (str, False),
        "Description": (str, False),
        "Expires": (double, False),
    }


class DeltaSyncConfig(AWSProperty):
    """
    `DeltaSyncConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html>`__
    """

    props: PropsDictType = {
        "BaseTableTTL": (str, True),
        "DeltaSyncTableName": (str, True),
        "DeltaSyncTableTTL": (str, True),
    }


class DynamoDBConfig(AWSProperty):
    """
    `DynamoDBConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html>`__
    """

    props: PropsDictType = {
        "AwsRegion": (str, True),
        "DeltaSyncConfig": (DeltaSyncConfig, False),
        "TableName": (str, True),
        "UseCallerCredentials": (boolean, False),
        "Versioned": (boolean, False),
    }


class ElasticsearchConfig(AWSProperty):
    """
    `ElasticsearchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html>`__
    """

    props: PropsDictType = {
        "AwsRegion": (str, True),
        "Endpoint": (str, True),
    }


class AwsIamConfig(AWSProperty):
    """
    `AwsIamConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html>`__
    """

    props: PropsDictType = {
        "SigningRegion": (str, False),
        "SigningServiceName": (str, False),
    }


class AuthorizationConfig(AWSProperty):
    """
    `AuthorizationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html>`__
    """

    props: PropsDictType = {
        "AuthorizationType": (str, True),
        "AwsIamConfig": (AwsIamConfig, False),
    }


class HttpConfig(AWSProperty):
    """
    `HttpConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html>`__
    """

    props: PropsDictType = {
        "AuthorizationConfig": (AuthorizationConfig, False),
        "Endpoint": (str, True),
    }


class LambdaConfig(AWSProperty):
    """
    `LambdaConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html>`__
    """

    props: PropsDictType = {
        "LambdaFunctionArn": (str, True),
    }


class OpenSearchServiceConfig(AWSProperty):
    """
    `OpenSearchServiceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html>`__
    """

    props: PropsDictType = {
        "AwsRegion": (str, True),
        "Endpoint": (str, True),
    }


class RdsHttpEndpointConfig(AWSProperty):
    """
    `RdsHttpEndpointConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html>`__
    """

    props: PropsDictType = {
        "AwsRegion": (str, True),
        "AwsSecretStoreArn": (str, True),
        "DatabaseName": (str, False),
        "DbClusterIdentifier": (str, True),
        "Schema": (str, False),
    }


class RelationalDatabaseConfig(AWSProperty):
    """
    `RelationalDatabaseConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html>`__
    """

    props: PropsDictType = {
        "RdsHttpEndpointConfig": (RdsHttpEndpointConfig, False),
        "RelationalDatabaseSourceType": (str, True),
    }


class DataSource(AWSObject):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html>`__
    """

    resource_type = "AWS::AppSync::DataSource"

    props: PropsDictType = {
        "ApiId": (str, True),
        "Description": (str, False),
        "DynamoDBConfig": (DynamoDBConfig, False),
        "ElasticsearchConfig": (ElasticsearchConfig, False),
        "HttpConfig": (HttpConfig, False),
        "LambdaConfig": (LambdaConfig, False),
        "Name": (str, True),
        "OpenSearchServiceConfig": (OpenSearchServiceConfig, False),
        "RelationalDatabaseConfig": (RelationalDatabaseConfig, False),
        "ServiceRoleArn": (str, False),
        "Type": (str, True),
    }


class DomainName(AWSObject):
    """
    `DomainName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html>`__
    """

    resource_type = "AWS::AppSync::DomainName"

    props: PropsDictType = {
        "CertificateArn": (str, True),
        "Description": (str, False),
        "DomainName": (str, True),
    }


class DomainNameApiAssociation(AWSObject):
    """
    `DomainNameApiAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html>`__
    """

    resource_type = "AWS::AppSync::DomainNameApiAssociation"

    props: PropsDictType = {
        "ApiId": (str, True),
        "DomainName": (str, True),
    }


class LambdaConflictHandlerConfig(AWSProperty):
    """
    `LambdaConflictHandlerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html>`__
    """

    props: PropsDictType = {
        "LambdaConflictHandlerArn": (str, False),
    }


class SyncConfig(AWSProperty):
    """
    `SyncConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html>`__
    """

    props: PropsDictType = {
        "ConflictDetection": (str, True),
        "ConflictHandler": (str, False),
        "LambdaConflictHandlerConfig": (LambdaConflictHandlerConfig, False),
    }


class FunctionConfiguration(AWSObject):
    """
    `FunctionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html>`__
    """

    resource_type = "AWS::AppSync::FunctionConfiguration"

    props: PropsDictType = {
        "ApiId": (str, True),
        "DataSourceName": (str, True),
        "Description": (str, False),
        "FunctionVersion": (str, True),
        "Name": (str, True),
        "RequestMappingTemplate": (str, False),
        "RequestMappingTemplateS3Location": (str, False),
        "ResponseMappingTemplate": (str, False),
        "ResponseMappingTemplateS3Location": (str, False),
        "SyncConfig": (SyncConfig, False),
    }


class CognitoUserPoolConfig(AWSProperty):
    """
    `CognitoUserPoolConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html>`__
    """

    props: PropsDictType = {
        "AppIdClientRegex": (str, False),
        "AwsRegion": (str, False),
        "UserPoolId": (str, False),
    }


class LambdaAuthorizerConfig(AWSProperty):
    """
    `LambdaAuthorizerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html>`__
    """

    props: PropsDictType = {
        "AuthorizerResultTtlInSeconds": (double, False),
        "AuthorizerUri": (str, False),
        "IdentityValidationExpression": (str, False),
    }


class OpenIDConnectConfig(AWSProperty):
    """
    `OpenIDConnectConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html>`__
    """

    props: PropsDictType = {
        "AuthTTL": (double, False),
        "ClientId": (str, False),
        "IatTTL": (double, False),
        "Issuer": (str, False),
    }


class AdditionalAuthenticationProvider(AWSProperty):
    """
    `AdditionalAuthenticationProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html>`__
    """

    props: PropsDictType = {
        "AuthenticationType": (str, True),
        "LambdaAuthorizerConfig": (LambdaAuthorizerConfig, False),
        "OpenIDConnectConfig": (OpenIDConnectConfig, False),
        "UserPoolConfig": (CognitoUserPoolConfig, False),
    }


class LogConfig(AWSProperty):
    """
    `LogConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsRoleArn": (str, False),
        "ExcludeVerboseContent": (boolean, False),
        "FieldLogLevel": (str, False),
    }


class UserPoolConfig(AWSProperty):
    """
    `UserPoolConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html>`__
    """

    props: PropsDictType = {
        "AppIdClientRegex": (str, False),
        "AwsRegion": (str, False),
        "DefaultAction": (str, False),
        "UserPoolId": (str, False),
    }


class GraphQLApi(AWSObject):
    """
    `GraphQLApi <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>`__
    """

    resource_type = "AWS::AppSync::GraphQLApi"

    props: PropsDictType = {
        "AdditionalAuthenticationProviders": (
            [AdditionalAuthenticationProvider],
            False,
        ),
        "AuthenticationType": (str, True),
        "LambdaAuthorizerConfig": (LambdaAuthorizerConfig, False),
        "LogConfig": (LogConfig, False),
        "Name": (str, True),
        "OpenIDConnectConfig": (OpenIDConnectConfig, False),
        "Tags": (Tags, False),
        "UserPoolConfig": (UserPoolConfig, False),
        "XrayEnabled": (boolean, False),
    }


class GraphQLSchema(AWSObject):
    """
    `GraphQLSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html>`__
    """

    resource_type = "AWS::AppSync::GraphQLSchema"

    props: PropsDictType = {
        "ApiId": (str, True),
        "Definition": (str, False),
        "DefinitionS3Location": (str, False),
    }


class CachingConfig(AWSProperty):
    """
    `CachingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html>`__
    """

    props: PropsDictType = {
        "CachingKeys": ([str], False),
        "Ttl": (double, False),
    }


class PipelineConfig(AWSProperty):
    """
    `PipelineConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html>`__
    """

    props: PropsDictType = {
        "Functions": ([str], False),
    }


class Resolver(AWSObject):
    """
    `Resolver <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html>`__
    """

    resource_type = "AWS::AppSync::Resolver"

    props: PropsDictType = {
        "ApiId": (str, True),
        "CachingConfig": (CachingConfig, False),
        "DataSourceName": (str, False),
        "FieldName": (str, True),
        "Kind": (resolver_kind_validator, False),
        "PipelineConfig": (PipelineConfig, False),
        "RequestMappingTemplate": (str, False),
        "RequestMappingTemplateS3Location": (str, False),
        "ResponseMappingTemplate": (str, False),
        "ResponseMappingTemplateS3Location": (str, False),
        "SyncConfig": (SyncConfig, False),
        "TypeName": (str, True),
    }
