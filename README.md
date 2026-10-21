# Intelligent and Trustworthy Judgment Algorithm based on File Extended Attributes

## Overview
This repository contains the core implementation of my first-author paper accepted at IEECT.  It addresses the security risks and performance loss caused by traditional rule-driven file trust marking mechanisms in Linux systems.

## Key Features & Methodology
System Implementation: Developed a Linux Security Module (LSM) hook and extended attribute (xattr) manipulation in C/C++for kernel-level file execution control.
Feature Engineering: Constructed a 7-dimensional feature system integrating both static and dynamic attributes using Python 3.9 scripts (e.g., file source, integrity measurement, operation behavior).
Hybrid ML Model: Designed a hybrid classification model combining rule-based logic and a Random Forest algorithm (via Scikit-learn) to dynamically update file trust labels.
Performance Optimization: Implemented lightweight strategies including rolling hash and caching mechanisms to drastically reduce system overhead.
System Evaluation: Verified model functionality and system performance using Unixbench on a dataset of 100,000+ file samples.

##  Experimental Results
Accuracy: Achieved 99.93% average accuracy in trust determination.
Performance Overhead: System performance loss strictly controlled within 5% (both single-thread and multi-thread).
Inference Latency: Average kernel-level response delay kept under 50μs.

##  Tech Stack
Languages: Python, C/C++
Machine Learning: Scikit-learn (Random Forest, Cross-validation)
Environment: Linux (Kernel 5.15), LSM Framework
Evaluation Tools: Unixbench, Custom Feature Collection Scripts

