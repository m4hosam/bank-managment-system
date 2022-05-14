--rejected
/*SELECT cus_id, ay, anapara, acpt_date
FROM loanRequests
WHERE cus_id = 303 and 
	acpt_date IS NULL;*/

--accepted
/*SELECT cus_id, ay, anapara, acpt_date
FROM loanRequests
WHERE cus_id = 302;*/


--expense transactions
/*SELECT * 
FROM transactions2 
WHERE trans_type = 'withdraw' or trans_type = 'loan takeout';*/

--income transactions
/*SELECT * 
FROM transactions2 
WHERE trans_type = 'deposit' or trans_type = 'loan payment';*/

/*SELECT SUM(total)
FROM transactions2 tr
WHERE trans_type = 'loan payment'

SELECT SUM(t2.total*exch_rate)
FROM transactions2 t2, account2 a, currency cur
WHERE (t2.trans_type = 'deposit' and
	t2.rsv_id = a.acc_id and
	cur.curr_code = a.currency)*/
	
--bank income
/*SELECT lp.total + dep.total bank_income
FROM (SELECT SUM(total) total
FROM transactions2 tr
WHERE trans_type = 'loan payment') as lp,
(SELECT SUM(t2.total*exch_rate) total
FROM transactions2 t2, account2 a, currency cur
WHERE (t2.trans_type = 'deposit' and
	t2.rsv_id = a.acc_id and
	cur.curr_code = a.currency)) as dep*/
	
			
--bank expense
/*SELECT lt.total + wd.total bank_expense
FROM (SELECT SUM(total) total
FROM transactions2 tr
WHERE trans_type = 'loan takeout') as lt,
(SELECT SUM(t2.total*exch_rate) total
FROM transactions2 t2, account2 a, currency cur
WHERE (t2.trans_type = 'withdraw' and
	t2.src_id = a.acc_id and
	cur.curr_code = a.currency)) as wd*/

--bank balance
/*SELECT SUM(balance * exch_rate) bank_balance
FROM account2 a, currency curr
WHERE a.currency = curr.curr_code*/


/*
UPDATE others
SET tarih = '2022-06-16'

UPDATE others
SET gecikme_faiz = 6.1

UPDATE others
SET clerk_salary = 5000

SELECT tarih
FROM others;

SELECT gecikme_faiz
FROM others;

SELECT clerk_salary
FROM others;*/
