---
layout: page
title: ELIDL - A Meta-Language for Representing Instructional Design in an E-learning Course
permalink: /elidl/
nomenu: true
---

### About

ELIDL (E-learning Instructional Design Meta-Language) is a language for specifying generic and domain-neutral instructional design. We represent instructional design as rules for sequencing and selection of learning content in a course.  Three main goals have been set for ELIDL - to be generic, expressive and machine-readable. ELIDL is an XML-based language and can be considered a meta-language for IMS Learning Design (IMS LD) specification. An instructional strategy represented using ELIDL may be applied to any learning content resulting in a concrete IMS LD course shaped according to the specified strategy.

### Examples

Here you can find some representative instructional strategies described using ELIDL.

#### No-sequencing
In this instructional strategy, the learner is free to choose learning activities at will, in any order and without any restrictions. No sequencing information is specified in this strategy (Chew and Hua, 2008). 

+ [no_sequencing.xml]({{ site.baseurl }}/files/other/elidl/no_sequencing.xml)

#### Linear

In this mode, the learner must progress through the contents in a pre-determined order.
The learner will start with the introduction first, then do all the lessons in a
linear order. The learner cannot proceed forward with the lessons until he has completed the current lesson. The student will be presented with a comprehensive exam or
quiz after he has completed all the lessons (Chew and Hua, 2008).

+ [linear.xml]({{ site.baseurl }}/files/other/elidl/linear.xml)

#### Knowledge-paced 

In this mode, the learner must go through and complete the introduction first. After that he
may proceed to the module 1 pre-test, select another module pre-test, or select a lesson.
The learner may ‘jump’ between modules, selecting pre-tests or lessons in any order. The learner cannot select the Module post-tests. These are only encountered after the learner ‘flows’ through the modules lessons. If the learner passes an exam (pre- or post-),
the module’s learning objective has been satisfied and the module’s post-test becomes
disabled (Chew and Hua 2008).

+ [knowledge_paced.xml]({{ site.baseurl }}/files/other/elidl/knowledge_paced.xml)

#### Remediation
In this mode, the learner must go through and complete the introduction, and then follow a
‘linear’ approach. If the learner passes (i.e. meets all of the lessons objectives) the post-test, the course is completed. For each lesson that is “not satisfied” on the post-test, the learner is directed to that associated lesson(s) of instructional content, and once completed, must retake the lesson post-test (Chew and Hua, 2008).

+ [remediation.xml]({{ site.baseurl }}/files/other/elidl/remediation.xml)

#### Competency assessment
The learner is first presented with an assessment that internally evaluates the learner’s mastery of each of the module objectives. The learner is then presented with the instructional material (modules) related to unsatisfied objectives. After the learner has completed all the required instructional materials, an exam is presented that re-tests the objectives the learner has not satisfied (Chew and Hua, 2008).

+ [competency_assessment.xml]({{ site.baseurl }}/files/other/elidl/competency_assessment.xml)

#### Project-based learning
This strategy consists of several phases:
1. Preliminary phase - introduction which covers general information about the course
2. Main phase - it includes preparing for the project, project development and several milestones for following learners' progress. 
3. Final phase - this phase includes project evaluation and grading

+ [project_based.xml]({{ site.baseurl }}/files/other/elidl/project_based.xml)

#### References
+ Chew, L.K., Hua, T.G. (2008). Instructional Strategies and Limitations of the SCORM 2004, in: Proceedings of the 16th International Conference on Computers in Education (ICCE 2008). Taipei, Taiwan, pp. 153 – 160.
+ Derntl, M., Motschnig-Pitrik, R. (2004). Patterns for blended, Person-Centered learning: strategy, concepts, experiences, and evaluation, in: Proceedings of the 2004 ACM Symposium on Applied Computing, SAC  ’04. ACM, New York, NY, USA, pp. 916–923.

### Evaluation

ELIDL was evaluated on the group of 16 participants. The following data collection instruments were used in the evaluation:

+ [Background_questionnaire]({{ site.baseurl }}/files/other/elidl/Background_questionnaire.pdf)
+ [Test 1]({{ site.baseurl }}/files/other/elidl/Test_1.pdf)
+ [Test 2]({{ site.baseurl }}/files/other/elidl/Test_2.pdf)
+ [Test 3]({{ site.baseurl }}/files/other/elidl/Test_3.pdf)
+ [Characteristic questionnaire]({{ site.baseurl }}/files/other/elidl/Characteristics_questionnaire.pdf)
