# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, Tags
from .validators import boolean, double, integer


class CsvOptions(AWSProperty):
    """
    `CsvOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html>`_
    """

    props = {
        "Delimiter": (str, False),
        "HeaderRow": (boolean, False),
    }


class ExcelOptions(AWSProperty):
    """
    `ExcelOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html>`_
    """

    props = {
        "HeaderRow": (boolean, False),
        "SheetIndexes": ([integer], False),
        "SheetNames": ([str], False),
    }


class JsonOptions(AWSProperty):
    """
    `JsonOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html>`_
    """

    props = {
        "MultiLine": (boolean, False),
    }


class FormatOptions(AWSProperty):
    """
    `FormatOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html>`_
    """

    props = {
        "Csv": (CsvOptions, False),
        "Excel": (ExcelOptions, False),
        "Json": (JsonOptions, False),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html>`_
    """

    props = {
        "Bucket": (str, True),
        "Key": (str, False),
    }


class DataCatalogInputDefinition(AWSProperty):
    """
    `DataCatalogInputDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html>`_
    """

    props = {
        "CatalogId": (str, False),
        "DatabaseName": (str, False),
        "TableName": (str, False),
        "TempDirectory": (S3Location, False),
    }


class DatabaseInputDefinition(AWSProperty):
    """
    `DatabaseInputDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html>`_
    """

    props = {
        "DatabaseTableName": (str, False),
        "GlueConnectionName": (str, True),
        "QueryString": (str, False),
        "TempDirectory": (S3Location, False),
    }


class Metadata(AWSProperty):
    """
    `Metadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-metadata.html>`_
    """

    props = {
        "SourceArn": (str, False),
    }


class Input(AWSProperty):
    """
    `Input <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html>`_
    """

    props = {
        "DataCatalogInputDefinition": (DataCatalogInputDefinition, False),
        "DatabaseInputDefinition": (DatabaseInputDefinition, False),
        "Metadata": (Metadata, False),
        "S3InputDefinition": (S3Location, False),
    }


class FilesLimit(AWSProperty):
    """
    `FilesLimit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html>`_
    """

    props = {
        "MaxFiles": (integer, True),
        "Order": (str, False),
        "OrderedBy": (str, False),
    }


class FilterValue(AWSProperty):
    """
    `FilterValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html>`_
    """

    props = {
        "Value": (str, True),
        "ValueReference": (str, True),
    }


class FilterExpression(AWSProperty):
    """
    `FilterExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html>`_
    """

    props = {
        "Expression": (str, True),
        "ValuesMap": ([FilterValue], True),
    }


class DatetimeOptions(AWSProperty):
    """
    `DatetimeOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html>`_
    """

    props = {
        "Format": (str, True),
        "LocaleCode": (str, False),
        "TimezoneOffset": (str, False),
    }


class DatasetParameter(AWSProperty):
    """
    `DatasetParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html>`_
    """

    props = {
        "CreateColumn": (boolean, False),
        "DatetimeOptions": (DatetimeOptions, False),
        "Filter": (FilterExpression, False),
        "Name": (str, True),
        "Type": (str, True),
    }


class PathParameter(AWSProperty):
    """
    `PathParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html>`_
    """

    props = {
        "DatasetParameter": (DatasetParameter, True),
        "PathParameterName": (str, True),
    }


class PathOptions(AWSProperty):
    """
    `PathOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html>`_
    """

    props = {
        "FilesLimit": (FilesLimit, False),
        "LastModifiedDateCondition": (FilterExpression, False),
        "Parameters": ([PathParameter], False),
    }


class Dataset(AWSObject):
    """
    `Dataset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html>`_
    """

    resource_type = "AWS::DataBrew::Dataset"

    props = {
        "Format": (str, False),
        "FormatOptions": (FormatOptions, False),
        "Input": (Input, True),
        "Name": (str, True),
        "PathOptions": (PathOptions, False),
        "Tags": (Tags, False),
    }


class DatabaseTableOutputOptions(AWSProperty):
    """
    `DatabaseTableOutputOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html>`_
    """

    props = {
        "TableName": (str, True),
        "TempDirectory": (S3Location, False),
    }


class S3TableOutputOptions(AWSProperty):
    """
    `S3TableOutputOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html>`_
    """

    props = {
        "Location": (S3Location, True),
    }


class DataCatalogOutput(AWSProperty):
    """
    `DataCatalogOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html>`_
    """

    props = {
        "CatalogId": (str, False),
        "DatabaseName": (str, True),
        "DatabaseOptions": (DatabaseTableOutputOptions, False),
        "Overwrite": (boolean, False),
        "S3Options": (S3TableOutputOptions, False),
        "TableName": (str, True),
    }


class DatabaseOutput(AWSProperty):
    """
    `DatabaseOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html>`_
    """

    props = {
        "DatabaseOptions": (DatabaseTableOutputOptions, True),
        "DatabaseOutputMode": (str, False),
        "GlueConnectionName": (str, True),
    }


class JobRecipe(AWSProperty):
    """
    `JobRecipe <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html>`_
    """

    props = {
        "Name": (str, True),
        "Version": (str, False),
    }


class JobSample(AWSProperty):
    """
    `JobSample <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html>`_
    """

    props = {
        "Mode": (str, False),
        "Size": (integer, False),
    }


class CsvOutputOptions(AWSProperty):
    """
    `CsvOutputOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html>`_
    """

    props = {
        "Delimiter": (str, False),
    }


class OutputFormatOptions(AWSProperty):
    """
    `OutputFormatOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html>`_
    """

    props = {
        "Csv": (CsvOutputOptions, False),
    }


class Output(AWSProperty):
    """
    `Output <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html>`_
    """

    props = {
        "CompressionFormat": (str, False),
        "Format": (str, False),
        "FormatOptions": (OutputFormatOptions, False),
        "Location": (S3Location, True),
        "Overwrite": (boolean, False),
        "PartitionColumns": ([str], False),
    }


class OutputLocation(AWSProperty):
    """
    `OutputLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html>`_
    """

    props = {
        "Bucket": (str, True),
        "Key": (str, False),
    }


class ColumnSelector(AWSProperty):
    """
    `ColumnSelector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html>`_
    """

    props = {
        "Name": (str, False),
        "Regex": (str, False),
    }


class StatisticOverride(AWSProperty):
    """
    `StatisticOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html>`_
    """

    props = {
        "Parameters": (dict, True),
        "Statistic": (str, True),
    }


class StatisticsConfiguration(AWSProperty):
    """
    `StatisticsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html>`_
    """

    props = {
        "IncludedStatistics": ([str], False),
        "Overrides": ([StatisticOverride], False),
    }


class ColumnStatisticsConfiguration(AWSProperty):
    """
    `ColumnStatisticsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html>`_
    """

    props = {
        "Selectors": ([ColumnSelector], False),
        "Statistics": (StatisticsConfiguration, True),
    }


class AllowedStatistics(AWSProperty):
    """
    `AllowedStatistics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-allowedstatistics.html>`_
    """

    props = {
        "Statistics": ([str], True),
    }


class EntityDetectorConfiguration(AWSProperty):
    """
    `EntityDetectorConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html>`_
    """

    props = {
        "AllowedStatistics": (AllowedStatistics, False),
        "EntityTypes": ([str], True),
    }


class ProfileConfiguration(AWSProperty):
    """
    `ProfileConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html>`_
    """

    props = {
        "ColumnStatisticsConfigurations": ([ColumnStatisticsConfiguration], False),
        "DatasetStatisticsConfiguration": (StatisticsConfiguration, False),
        "EntityDetectorConfiguration": (EntityDetectorConfiguration, False),
        "ProfileColumns": ([ColumnSelector], False),
    }


class ValidationConfiguration(AWSProperty):
    """
    `ValidationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html>`_
    """

    props = {
        "RulesetArn": (str, True),
        "ValidationMode": (str, False),
    }


class Job(AWSObject):
    """
    `Job <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html>`_
    """

    resource_type = "AWS::DataBrew::Job"

    props = {
        "DataCatalogOutputs": ([DataCatalogOutput], False),
        "DatabaseOutputs": ([DatabaseOutput], False),
        "DatasetName": (str, False),
        "EncryptionKeyArn": (str, False),
        "EncryptionMode": (str, False),
        "JobSample": (JobSample, False),
        "LogSubscription": (str, False),
        "MaxCapacity": (integer, False),
        "MaxRetries": (integer, False),
        "Name": (str, True),
        "OutputLocation": (OutputLocation, False),
        "Outputs": ([Output], False),
        "ProfileConfiguration": (ProfileConfiguration, False),
        "ProjectName": (str, False),
        "Recipe": (JobRecipe, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "Timeout": (integer, False),
        "Type": (str, True),
        "ValidationConfigurations": ([ValidationConfiguration], False),
    }


class Sample(AWSProperty):
    """
    `Sample <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html>`_
    """

    props = {
        "Size": (integer, False),
        "Type": (str, True),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html>`_
    """

    resource_type = "AWS::DataBrew::Project"

    props = {
        "DatasetName": (str, True),
        "Name": (str, True),
        "RecipeName": (str, True),
        "RoleArn": (str, True),
        "Sample": (Sample, False),
        "Tags": (Tags, False),
    }


class SecondaryInput(AWSProperty):
    """
    `SecondaryInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html>`_
    """

    props = {
        "DataCatalogInputDefinition": (DataCatalogInputDefinition, False),
        "S3InputDefinition": (S3Location, False),
    }


class RecipeParameters(AWSProperty):
    """
    `RecipeParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html>`_
    """

    props = {
        "AggregateFunction": (str, False),
        "Base": (str, False),
        "CaseStatement": (str, False),
        "CategoryMap": (str, False),
        "CharsToRemove": (str, False),
        "CollapseConsecutiveWhitespace": (str, False),
        "ColumnDataType": (str, False),
        "ColumnRange": (str, False),
        "Count": (str, False),
        "CustomCharacters": (str, False),
        "CustomStopWords": (str, False),
        "CustomValue": (str, False),
        "DatasetsColumns": (str, False),
        "DateAddValue": (str, False),
        "DateTimeFormat": (str, False),
        "DateTimeParameters": (str, False),
        "DeleteOtherRows": (str, False),
        "Delimiter": (str, False),
        "EndPattern": (str, False),
        "EndPosition": (str, False),
        "EndValue": (str, False),
        "ExpandContractions": (str, False),
        "Exponent": (str, False),
        "FalseString": (str, False),
        "GroupByAggFunctionOptions": (str, False),
        "GroupByColumns": (str, False),
        "HiddenColumns": (str, False),
        "IgnoreCase": (str, False),
        "IncludeInSplit": (str, False),
        "Input": (dict, False),
        "Interval": (str, False),
        "IsText": (str, False),
        "JoinKeys": (str, False),
        "JoinType": (str, False),
        "LeftColumns": (str, False),
        "Limit": (str, False),
        "LowerBound": (str, False),
        "MapType": (str, False),
        "ModeType": (str, False),
        "MultiLine": (boolean, False),
        "NumRows": (str, False),
        "NumRowsAfter": (str, False),
        "NumRowsBefore": (str, False),
        "OrderByColumn": (str, False),
        "OrderByColumns": (str, False),
        "Other": (str, False),
        "Pattern": (str, False),
        "PatternOption1": (str, False),
        "PatternOption2": (str, False),
        "PatternOptions": (str, False),
        "Period": (str, False),
        "Position": (str, False),
        "RemoveAllPunctuation": (str, False),
        "RemoveAllQuotes": (str, False),
        "RemoveAllWhitespace": (str, False),
        "RemoveCustomCharacters": (str, False),
        "RemoveCustomValue": (str, False),
        "RemoveLeadingAndTrailingPunctuation": (str, False),
        "RemoveLeadingAndTrailingQuotes": (str, False),
        "RemoveLeadingAndTrailingWhitespace": (str, False),
        "RemoveLetters": (str, False),
        "RemoveNumbers": (str, False),
        "RemoveSourceColumn": (str, False),
        "RemoveSpecialCharacters": (str, False),
        "RightColumns": (str, False),
        "SampleSize": (str, False),
        "SampleType": (str, False),
        "SecondInput": (str, False),
        "SecondaryInputs": ([SecondaryInput], False),
        "SheetIndexes": ([integer], False),
        "SheetNames": ([str], False),
        "SourceColumn": (str, False),
        "SourceColumn1": (str, False),
        "SourceColumn2": (str, False),
        "SourceColumns": (str, False),
        "StartColumnIndex": (str, False),
        "StartPattern": (str, False),
        "StartPosition": (str, False),
        "StartValue": (str, False),
        "StemmingMode": (str, False),
        "StepCount": (str, False),
        "StepIndex": (str, False),
        "StopWordsMode": (str, False),
        "Strategy": (str, False),
        "TargetColumn": (str, False),
        "TargetColumnNames": (str, False),
        "TargetDateFormat": (str, False),
        "TargetIndex": (str, False),
        "TimeZone": (str, False),
        "TokenizerPattern": (str, False),
        "TrueString": (str, False),
        "UdfLang": (str, False),
        "Units": (str, False),
        "UnpivotColumn": (str, False),
        "UpperBound": (str, False),
        "UseNewDataFrame": (str, False),
        "Value": (str, False),
        "Value1": (str, False),
        "Value2": (str, False),
        "ValueColumn": (str, False),
        "ViewFrame": (str, False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html>`_
    """

    props = {
        "Operation": (str, True),
        "Parameters": (RecipeParameters, False),
    }


class ConditionExpression(AWSProperty):
    """
    `ConditionExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html>`_
    """

    props = {
        "Condition": (str, True),
        "TargetColumn": (str, True),
        "Value": (str, False),
    }


class RecipeStep(AWSProperty):
    """
    `RecipeStep <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html>`_
    """

    props = {
        "Action": (Action, True),
        "ConditionExpressions": ([ConditionExpression], False),
    }


class Recipe(AWSObject):
    """
    `Recipe <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html>`_
    """

    resource_type = "AWS::DataBrew::Recipe"

    props = {
        "Description": (str, False),
        "Name": (str, True),
        "Steps": ([RecipeStep], True),
        "Tags": (Tags, False),
    }


class SubstitutionValue(AWSProperty):
    """
    `SubstitutionValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html>`_
    """

    props = {
        "Value": (str, True),
        "ValueReference": (str, True),
    }


class Threshold(AWSProperty):
    """
    `Threshold <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html>`_
    """

    props = {
        "Type": (str, False),
        "Unit": (str, False),
        "Value": (double, True),
    }


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html>`_
    """

    props = {
        "CheckExpression": (str, True),
        "ColumnSelectors": ([ColumnSelector], False),
        "Disabled": (boolean, False),
        "Name": (str, True),
        "SubstitutionMap": ([SubstitutionValue], False),
        "Threshold": (Threshold, False),
    }


class Ruleset(AWSObject):
    """
    `Ruleset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html>`_
    """

    resource_type = "AWS::DataBrew::Ruleset"

    props = {
        "Description": (str, False),
        "Name": (str, True),
        "Rules": ([Rule], True),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
    }


class Schedule(AWSObject):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html>`_
    """

    resource_type = "AWS::DataBrew::Schedule"

    props = {
        "CronExpression": (str, True),
        "JobNames": ([str], False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
