; Definitions
(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define pi 3.14)

(define (abs x) 
    (if (< x 0) (- x) x)
)

; lambda
(define sum-square 
    (lambda (x y) (+ (square x) (square y)))
)


; more special form
; cond
(define (fib n)
    (cond ( (= n 0) 0 )
          ( (= n 1) 1 )
          ( else (+ (fib (- n 1)) (fib (- n 2))) )
    )
)

; begin
(begin (print 1) (print 2) 3 4)


; let 
( let ((a 3) (b 4))  (sum-square a b ) )


; Linked List
(define a (cons 1 (cons 2 (cons 3 (cons 4 nil)))))


: Quotations
(define a 1)
(define b 2)
(list a b)
(list 'a b)
(list 'a 'b)


(define (sum-while starting-x while-condition add-to-total update-x)
    `(begin 
        (define (f x total)
            (if, while-condition
                (f, update-x (+ total ,arr-to-total))
                total
            )
        )
        (f ,starting-x 0)
    )
)