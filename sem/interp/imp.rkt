#lang plai

;; IAE = <num> | {+ <IAE> <AE> } | {- <IAE> <IAE>} | <id>

(define-type IAE
  [num (n number?)]
  [add (left IAE?)
       (right IAE?)]
  [sub (left IAE?)
       (right IAE?)]
  [id (name symbol?)])

;; parse-exp: s-expr -> IAE
;; (parse '{+ 3 4}) -> (add (num 3) (num 4))

(define (parse-exp input)
  (cond
    [(number? input) (num input)]
    [(symbol? input) (id input)]
    [(and (= 3 (length input))
          (eq? (first input) '+))
     (add (parse-exp (second input))
          (parse-exp (third input)))]
    [(and (= 3 (length input))
          (eq? (first input) '-))
     (sub (parse-exp (second input))
          (parse-exp (third input)))]
    [else (error 'parse "syntax error")]))

;; IMP = {if <IAE> <IMP> <IMP>} | {while <IAE> <IMP>} | {set <id> <IAE>}
;;       | {print <IAE>} | {<IMP> <IMP>...} | {skip}

(define-type IMP
  [cif (cond IAE?)
      (true IMP?)
      (false IMP?)]
  [whl (cond IAE?)
         (body IMP?)]
  [st (lval symbol?)
      (rval IAE?)]
  [prt (exp IAE?)]
  [skip]
  [seq (cmd1 IMP?)
       (cmd2 IMP?)])
  
(define (parse-cmd input)
  (cond
    [(eq? (first input) 'if)
     (cif (parse-exp (second input))
          (parse-cmd (third input))
          (parse-cmd (fourth input)))]
    [(eq? (first input) 'while)
     (whl (parse-exp (second input))
            (parse-cmd (third input)))]
    [(eq? (first input) 'set)
     (st (second input)
         (parse-exp (third input)))]
    [(eq? (first input) 'print)
     (prt (parse-exp (second input)))]
    [(eq? (first input) 'skip)
     (skip)]
    [else (foldr seq (skip) (map parse-cmd input))]))

(define-type Env
  [env-empty]
  [env-entry (name symbol?)
             (val number?)
             (next Env?)])

;; lookup-env : ID Env -> num
(define (lookup-env name env)
  (type-case Env env
    [env-empty () 0]
    [env-entry (id val next) (if (symbol=? id name)
                                 val
                                 (lookup-env name next))])) 

;; interp-exp: IAE Env -> num

(define (interp-exp iae env)
  (type-case IAE iae
    [num (n) n]
    [id (name) (lookup-env name env)]
    [add (left right) (+ (interp-exp left env)
                         (interp-exp right env))]
    [sub (left right) (- (interp-exp left env)
                         (interp-exp right env))]))

;; interp-cmd: IMP Env -> Env

(define (interp-cmd imp env)
  (type-case IMP imp
    [skip () env]
    [st (lval rval)
        (env-entry lval
                   (interp-exp rval env) 
                   env)]
    [cif (cond true false)
         (if (= 0 (interp-exp cond env))
             (interp-cmd false env)
             (interp-cmd true env))]
    [whl (cond body)
         (if (= 0 (interp-exp cond env))
             env
             (interp-cmd imp (interp-cmd body env)))]
    [prt (exp) 
         (local () 
           (print (interp-exp exp env))
           (newline)
           env)]
    [seq (cmd1 cmd2)
         (interp-cmd cmd2 (interp-cmd cmd1 env))]))

(define (interp cmd)
    (interp-cmd (parse-cmd cmd) (env-empty)))
                
(interp '{{set x 3}
          {set y 2}
          {while x
            {{set y {+ y y}}
             {if {- x 1}
                 {skip}
                 {print 42}}
             {set x {- x 1}}}}
          {print y}})
       