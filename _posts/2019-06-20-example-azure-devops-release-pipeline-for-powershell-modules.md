---
title: Machine Learning Basic_1
description: ML fundamentals
categories:
  - machine-learning
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Key Terminology
# header:
#   image: /assets/images/logos/logo-text-8c3ba8a6.svg
---

## Introduction

Why machine learning? Many industry companies use machine learning to be specialized and differentiated by intelligent applications. For instance, early days, Amazon disrupted the retail market by introducing product recommendations to their website, Google disrupted the advertising market by targeting the new customers who have similar behaviors to the existing customers, and Uber disrupted the taxi industry by optimizing how to connect drivers with customers in real time. Such tech made their products special.

## Machine Learning Pipeline

ML pipeline is simply to train a model. Machine learning pipelines iteratively and  as every step is repeated to continuously improve the accuracy of the model and achieve a successful algorithm. To build better machine learning models, and get the most value from them, accessible, scalable and durable storage solutions are imperative, paving the way for on-premises object storage.

The purpose of this Release Pipeline is to take Artifacts from the Build Pipeline, and release them to a stage.
Here's an [example release](https://dev.azure.com/adamrushuk/PoC/_releaseProgress?_a=release-pipeline-progress&releaseId=30)
showing deployments to all three stages (Dev, Test, and Prod).

![Example Release](/assets/images/powershell-release-pipeline/example-release.png)

### Artifacts

In the Release section above you can see the PowerShellPipeline Artifacts appear under the Continuous deployment
heading. This shows a Release is triggered every time a Build Pipeline creates those Artifacts.

### Dev Stage

We now move on to the stages. Note there is a line between Artifacts and the Dev stage, due to a Pre-deployment
condition trigger set to After release:

![After release Pre-deployment condition trigger](/assets/images/powershell-release-pipeline/pre-deployment-condition-trigger.png)

This setting ensures the Dev stage is triggered automatically without user intervention.

### Test Stage

The Test stage trigger is configured to start after the previous Dev stage, using an After stage trigger:
![After stage Pre-deployment condition trigger](/assets/images/powershell-release-pipeline/after-stage-pre-deployment-condition-trigger.png)

### Prod Stage

Lastly, the Prod stage has a Manual only trigger:
![Manual Pre-deployment condition trigger](/assets/images/powershell-release-pipeline/manual-pre-deployment-condition-trigger.png)

This gives us the option to manually validate the Dev and Test environments are working as expected before we
release to Prod.

## Stage Tasks

All stages use roughly the same tasks, but let's take a closer look into Prod:
![Stage Tasks](/assets/images/powershell-release-pipeline/stage-tasks.png)

### Install NuGet

The Install NuGet task is self-explanatory, and simply installs the specified NuGet binary version. NuGet is
required to publish PowerShell modules to our internal Artifact feed.

### Additional Integration Tests for Prod Environment

This task is a placeholder for actual test code, just to highlight you *could* run integration tests at this point
if required. This might include provisioning infrastructure, loading data, then running tests and publishing the
test results.

### Publish Module to Artifact Feed (prod)

The final task is responsible for running a PowerShell script called `Publish-AzDOArtifactFeed.ps1`, which takes
two parameters: `AzDOArtifactFeedName` and `AzDOPat`:

![Publish Module Task](/assets/images/powershell-release-pipeline/publish-module-task.png)

The Arguments field shown above references Pipeline Variables `$(artifact_feed_name)` and `$(artifact_feed_pat)`,
shown below:

![Pipeline Variables](/assets/images/powershell-release-pipeline/pipeline-variables.png)

## Publish-AzDOArtifactFeed.ps1

The code below has comments throughout, but the main steps are:

1. Register a NuGet Package Source.
1. Register a PowerShell Repository.
1. Publish a PowerShell module.

{% gist 891f287fb27f0df378d696f366c3fa61 Publish-AzDOArtifactFeed.ps1 %}

## Azure Artifacts Feed

Once the PowerShell module has been published by the `Publish-AzDOArtifactFeed.ps1` script, the new NuGet package
is available within the specified Azure Artifacts feed (eg. prod):

![Azure Artifacts Feed](/assets/images/powershell-release-pipeline/azure-artifacts-feed.png)
