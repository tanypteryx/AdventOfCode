;;;; AoC 2021, Day 1

;;; get general purpose library
(load "../../lib/lisp/advent-of-code.lisp")

(defun consecutive-diff (data)
  (mapcar #'- (rest data) data))

;; count occurence of positive numbers in a list
(defun count-positive-numbers (data)
  (let ((count 0))
    (mapcar (lambda (x) (when (> x 0) (incf count))) data)
    count))

;; calculate running sum 
(defun running-sum (data window-size)
  (let ((length (length data)))
    (mapcar (lambda (i)
              (reduce #'+ (subseq data i (+ i window-size))))
            (loop for i from 0 to (- length window-size) collect i))))

;; not used, but let's generalize it
(defun moving-average (data window-size)
  (mapcar (lambda (i) 
	    (/ i window-size)) (running-sum data window-size)))


;; Here's the whole magic
(defun part1 (data)
  (count-positive-numbers  (consecutive-diff data)))

(defun part2 (data)
  (count-positive-numbers  (consecutive-diff (running-sum data 3))))

;;; Calling the functions for results 
;; parse to list of integers
(defparameter *data* (mapcar #'parse-integer (aoc:read-file-to-list "input.txt")))

;; solutions
(format t "Solution to Part 1: ~d~%"  (part1 *data*))
(format t "Solution to Part 2: ~d~%"  (part2 *data*))
