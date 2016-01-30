---
layout: page
title: A Model-Driven Course Management System
permalink: /corms/
nomenu: true
---

### About
This research applies techniques of the model-driven software development to the development and management of e-courses. Within the research, we have developed a course management system based on a platform-independent course model. The model consists of the three main components: learning objectives, learning resources and instructional design. Based on these three platform-independent source components, the system generates final courses in the following platform-specific formats: IMS LD, SCORM, LAMS and Sakai.

### Course Model

#### Learning Objectives

The model of learning objectives has been implemented using ontology. The main ontology classes and object properties are illustrated in the figure.

![Learning Objectives]({{ site.baseurl }}/files/other/corms/img_objectives_model.png)

The corresponding owl file is available [here]({{ site.baseurl }}/files/other/corms/objectives_model.owl)

#### Learning Resources

The model uses [IMS Content Packaging](https://www.imsglobal.org/content/packaging/index.html) specification for the formal representation of learning resources.

#### Instructional Strategy

The model represents an instructional strategy in a course using ELIDL (E-Learning Instructional Design Meta-Language). The XML schema of ELIDL is shown below.

![ELIDL Schema Part 1]({{ site.baseurl }}/files/other/corms/img_elidl_schema_1.png)

![ELIDL Schema Part 2]({{ site.baseurl }}/files/other/corms/img_elidl_schema_2.png)

The schema elements are explained in the following table.

![ELIDL Schema Explanation]({{ site.baseurl }}/files/other/corms/img_elidl_table_1.png)

![ELIDL Schema Explanation]({{ site.baseurl }}/files/other/corms/img_elidl_table_2.png)

The elements of the {expressions} schema group are explained below.

![ELIDL Schema Explanation]({{ site.baseurl }}/files/other/corms/img_elidl_expressions.png)

### Case Study

The course management system has been evaluated on the Web programming course taught at University of Novi Sad. Here you can find the components of the Web programming course formally represented using our course model. 

+ [Web programming - learning objectives]({{ site.baseurl }}/files/other/corms/wp_objectives.owl)
+ [Web programming - learning resources](https://dl.dropboxusercontent.com/u/33159784/corms/wp_resources.zip)
+ [Instructional strategy - no-sequencing]({{ site.baseurl }}/files/other/corms/is_no-sequencing.xml)
+ [Instructional strategy - linear]({{ site.baseurl }}/files/other/corms/is_linear.xml)
+ [Instructional strategy - knowledge-paced]({{ site.baseurl }}/files/other/corms/is_knowledge_paced.xml)
+ [Instructional strategy - remediation]({{ site.baseurl }}/files/other/corms/is_remediation.xml)
+ [Instructional strategy - competency-assessment]({{ site.baseurl }}/files/other/corms/is_competency_assessment.xml)
+ [Instructional strategy - project-based learning]({{ site.baseurl }}/files/other/corms/is_project_based.xml)

Based on the model of the Web programming course, the system has generated following courses.

+ [IMS LD course (based on the no sequencing instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_noseq.zip)

+ [IMS LD course (based on the linear instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_linear.zip)

+ [IMS LD course (based on the knowledge paced instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_knowledge_paced.zip)

+ [IMS LD course (based on the remediation instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_remediation.zip)

+ [IMS LD course (based on the competency assessment instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_comp_assess.zip)

+ [IMS LD course (based on the project-based learning instructional strategy)](https://dl.dropboxusercontent.com/u/33159784/corms/wp_imsld_project_based.zip)

+ [SCORM course](https://dl.dropboxusercontent.com/u/33159784/corms/wp_scorm.zip)

+ [LAMS course](https://dl.dropboxusercontent.com/u/33159784/corms/wp_lams.zip)

+ [Sakai course](https://dl.dropboxusercontent.com/u/33159784/corms/wp_sakai.zip)