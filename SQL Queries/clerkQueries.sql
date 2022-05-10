--displays new customers***********************************************
/*
SELECT *
FROM customer c
WHERE c.cus_status = 'NEW';*/

--logic desices which clerk should be assigned the new customer
--assigns clerk to customer*********************************************
/*
INSERT INTO customerClerks (cus_id, clrk_id)
VALUES({cus_id}, {clrk_id});*/

--displays all customers belonging to a clerk***************************
/*
SELECT cus.id, cus.firstN, cus.lastN, phone, TC, Adress
FROM customer cus, customerClerks cusClrk, clerk
WHERE clerk.id = cusClrk.clrk_id and
	cus.id = cusClrk.cus_id and
	cusClrk.clrk_id = {clerk id};*/

--all transactions made by the clerk's customers************************
/*SELECT distinct c.id, tr.trans_no, src_id , rsv_id, trans_type
FROM transactions tr, userAccounts ua, account a, customer c
WHERE c.id = ua.cus_id and
	a.acc_id = ua.acc_id and
	(tr.src_id = a.acc_id or tr.cus_id = c.id) and 
	c.id in(
		SELECT cus.id
		FROM customer cus, customerClerks cusClrk, clerk
		WHERE clerk.id = cusClrk.clrk_id and
			cus.id = cusClrk.cus_id and
			cusClrk.clrk_id = {clerk id}
		);*/


--delete own customer**************************************************
/*
DELETE customer
FROM customer c
WHERE c.id = {customer id} and c.id IN(
						SELECT cus.id
						FROM customer cus, customerClerks cusClrk, clerk
						WHERE clerk.id = cusClrk.clrk_id and
							cus.id = cusClrk.cus_id and
							cusClrk.clrk_id = {clerk id});*/

--clerk can delete accounts of his/her own customers (assosiated transactions will also be deleted)
--note: query does not check if balance is 0 --> should be checked by logic*********************
/*
DELETE account
FROM account a
WHERE a.acc_id = 901 and
	a.acc_id IN(
		SELECT a.acc_id
		FROM account a, userAccounts ua, customer c
		WHERE a.acc_id = ua.acc_id and
			ua.cus_id = c.id and
			c.id IN(
				SELECT cus.id
				FROM customer cus, customerClerks cusClrk, clerk
				WHERE clerk.id = cusClrk.clrk_id and
					cus.id = cusClrk.cus_id and
					cusClrk.clrk_id = 3)
				);*/

--displays clerk's customer's accounts***************************
/*
SELECT a.acc_id
		FROM account a, userAccounts ua, customer c
		WHERE a.acc_id = ua.acc_id and
			ua.cus_id = c.id and
			c.id IN(
				SELECT cus.id
				FROM customer cus, customerClerks cusClrk, clerk
				WHERE clerk.id = cusClrk.clrk_id and
					cus.id = cusClrk.cus_id and
					cusClrk.clrk_id = 3);*/


--SELECTS ALL TRANSACTIONS WHERE THE SOURCE IS AN ACCOUNT BELONGING TO ONE OF THE CLERK'S CUSTOMERS, ALSO DISPLAYS THE CUS_ID AND ACCOUNT BALANCE
/*SELECT tr.trans_date,tr.src_id as src_acc, trans_type, total, ua.cus_id, a.balance
FROM transactions2 tr
LEFT JOIN userAccounts2 ua
ON ua.acc_id = tr.src_id 
LEFT JOIN account2 a
ON a.acc_id = tr.src_id
WHERE tr.src_id IN(SELECT ua.acc_id
		FROM userAccounts2 ua, customer2 c
		WHERE c.id = ua.cus_id and
			ua.cus_id IN (SELECT c.id
					FROM customer2 c, customerClerks2 cc
					WHERE c.id = cc.cus_id and
						clerk_id = {clerk_id}))
*/

--expense
SELECT DISTINCT ua.cus_id, tr.*, total * exch_rate
FROM transactions2 tr, currency curr, account2 a, userAccounts2 ua
WHERE ua.acc_id = tr.src_id and
	tr.src_id = a.acc_id and
	a.currency = curr.curr_code;

--income
SELECT DISTINCT ua.cus_id, tr.*, total * exch_rate
FROM transactions2 tr, currency curr, account2 a, userAccounts2 ua
WHERE ua.acc_id = tr.rsv_id and
	tr.rsv_id = a.acc_id and
	a.currency = curr.curr_code;

--total balance
SELECT c.id,/*, a.acc_id,*/ SUM(exch_rate * balance)  as totalBalance
FROM currency cur, userAccounts2 ua, account2 a, customer2 c
WHERE ua.acc_id = a.acc_id and
		a.currency = cur.curr_code and
		c.id = ua.cus_id
GROUP BY(c.id)
