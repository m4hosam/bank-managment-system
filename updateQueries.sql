
--#shows transaction + source and recepient balances
SELECT trans_no,trans_date, src_id, rsv_id,trans_type,total, a1.balance src_balance, a2.balance rsv_balance FROM transactions tr
LEFT JOIN account a1
ON tr.src_id = a1.acc_id 
LEFT JOIN account a2
ON tr.rsv_id = a2.acc_id;

--#list all accounts that belong to the user*************************
SELECT c.id cus_id, a.acc_id, currency, balance
FROM customer c, account a, userAccounts ua
WHERE c.id = ua.cus_id and
	ua.acc_id = a.acc_id and
	c.id = 301 ;

--# list all information that belong to the user ---(Query)***********
SELECT * 
FROM customer
WHERE id = 301;

--# Filter all transactions of that user -order by date-**************
SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total, t.cus_id
FROM customer c, transactions t, account a, userAccounts ua
WHERE c.id = ua.cus_id and
	ua.acc_id = a.acc_id and
	(t.src_id = a.acc_id OR t.cus_id = c.id) and
	c.id = 301
ORDER BY(t.trans_date);*/


--==================================================================
/**
UPDATE INFO COMMANDS

***WARNING: always include WHERE clause or else ALL rows get updated***

*/

/*

--update PHONE*************************
UPDATE customer
SET customer.phone = {new phone number(string)}
WHERE customer.id = {customer id(int)};

--update EMAIL*************************

UPDATE customer
SET customer.email = {new email}
WHERE customer.id = {customer id(int)};

--update ADDRESS***********************

UPDATE customer
SET customer.Adress = {new address}
WHERE customer.id = {customer id(int)};

--update FIRSTNAME*********************

UPDATE customer
SET customer.firstN = {new firstN}
WHERE customer.id = {customer id(int)};

--update LASTNAME**********************

UPDATE customer
SET customer.lastN = {new lastN}
WHERE customer.id = {customer id(int)};

--update TC****************************

UPDATE customer
SET customer.TC = {new TC(string)}
WHERE customer.id = {customer id(int)};

--update BALANCE***********************

UPDATE ACCOUNT
SET account.balance = {new balance(float/int)}
WHERE account.acc_id = {customer id(int)}*/

--example for updating

--update PHONE
UPDATE customer
SET customer.phone = '324-789-3429'
WHERE customer.id = 301;

--update EMAIL
UPDATE customer
SET customer.email = 'x@email.com'
WHERE customer.id = 301;

--update ADDRESS
UPDATE customer
SET customer.Adress = 'X city'
WHERE customer.id = 301;

--update FIRSTNAME
UPDATE customer
SET customer.firstN = 'Charlie'
WHERE customer.id = 301;

--update LASTNAME
UPDATE customer
SET customer.lastN = 'Smith'
WHERE customer.id = 301;

--update TC
UPDATE customer
SET customer.TC = '943022030249'
WHERE customer.id = 301;

-- update BALANCE
UPDATE account
SET account.balance = 1000
WHERE account.acc_id = 901;