(defpackage :advent-of-code
  (:use :cl)
  (:nicknames :aoc)
  (:export
    #:read-file-to-list))

(in-package :advent-of-code)

(defun read-file-to-list (filename)
  "Reads a newline-seprated file named filename into a list of lines."
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
	  while line
	  collect line)))

