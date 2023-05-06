## About
This progress bar is a simple library that I started to visualize runtime statistics and predictions when running simulated annealing and genetic algorithms for an Introduction to Artifical Intelligence course I took during my senior year in 2023.

## Purpose
The purpose is to provide statistics and estimated runtime in the console for any loop when provided iteration and total iteration arguments.

Many similar and more comprehensive libraries surely exist. This is primarily an exercise for my personal development to learn how to set up and export Python libraries, maintain and develop a functional tool using git on the github platform.

## TBD:
- format README markdown
- write test suite
- improve and debug output (not all statistics accurately reflect their intended values currently)
- improve stylization
- add configuration options for display such as statistics (time formats), progress bar stylization (colors, flexible sizing, 'animations')

## Known Bugs:
- Console window must be at minimum x characters wide for output to display correctly and rewrite lines as intended
- line_clear() is not properly set up, conflicts with any output printed in loop
- average loop time is not an average, but shows time delta for just the last loop

## Author:
@fairlyaverage
