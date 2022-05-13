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


--SELECTS ALL TRANSACTIONS + SOURCE AND RECIEVE CUSTOMER ID AND BALANCE
SELECT DISTINCT trans_date, ua1.cus_id src_cus, ua2.cus_id rsv_cus, src_id, rsv_id, trans_type, total, (a1.balance - total) src_balance, (a2.balance + total *(ISNULL(c1.exch_rate,c2.exch_rate) / (ISNULL(c2.exch_rate,c1.exch_rate)))) as rsv_balance 
FROM transactions2 tr
LEFT JOIN account2 a1
ON tr.src_id = a1.acc_id
LEFT JOIN account2 a2
ON tr.rsv_id = a2.acc_id
LEFT JOIN userAccounts2 ua1
ON ua1.acc_id = src_id
LEFT JOIN userAccounts2 ua2
ON ua2.acc_id = rsv_id
LEFT JOIN currency c1
ON c1.curr_code = a1.currency
LEFT JOIN currency c2
ON c2.curr_code = a2.currency
WHERE ua1.cus_id = {cus_id} or ua2.cus_id = {cus_id};


--expense
SELECT DISTINCT ua.cus_id, SUM(total * ISNULL(exch_rate,1))
FROM transactions2 tr, currency curr, account2 a, userAccounts2 ua
WHERE ua.acc_id = tr.src_id and
    tr.src_id = a.acc_id and
    a.currency = curr.curr_code
    and (rsv_id NOT IN (SELECT acc_id
                        FROM userAccounts2 ua2 
                        WHERE ua.cus_id = ua2.cus_id)
    OR rsv_id IS NULL) and ua.cus_id = 302
GROUP BY(ua.cus_id) ORDER BY ua.cus_id;

--income
SELECT t1.cus_id, SUM(ISNULL(t1.income, 0) + ISNULL(t2.income,0))
FROM (SELECT ua2.cus_id , SUM(total * c1.exch_rate) income
FROM transactions2 tr, account2 a1, account2 a2, userAccounts2 ua1, userAccounts2 ua2, currency c1, currency c2
WHERE tr.src_id = a1.acc_id and
tr.rsv_id = a2.acc_id and
ua1.acc_id = src_id and
ua2.acc_id = rsv_id and
c1.curr_code = a1.currency and 
c2.curr_code = a2.currency and src_id not in(SELECT acc_id
					FROM userAccounts2 ua
					WHERE ua.cus_id = ua2.cus_id)
GROUP BY(ua2.cus_id)) t1
FULL OUTER JOIN (
SELECT ua1.cus_id, SUM(total * c1.exch_rate) income
FROM transactions2 tr, account2 a1, userAccounts2 ua1, currency c1
WHERE src_id IS NULL and
rsv_id = ua1.acc_id and
ua1.acc_id = a1.acc_id and
a1.currency = c1.curr_code
GROUP BY(ua1.cus_id)) t2 on t2.cus_id = t1.cus_id, customerClerks2 cc
WHERE t1.cus_id = cc.cus_id and
cc.clerk_id = {self.clerk_id}
GROUP BY(t1.cus_id) ORDER BY t1.cus_id;

--total balance
SELECT c.id, SUM(exch_rate * balance)  as totalBalance
FROM currency cur, userAccounts2 ua, account2 a, customer2 c
WHERE ua.acc_id = a.acc_id and
a.currency = cur.curr_code and
c.id = ua.cus_id and 
c.id = 301

GROUP BY(c.id) ORDER BY c.id
--TRANSACTIONS BY CLERK'S CUSTOMERS + CUSTOMER ID'S
/*SELECT DISTINCT tr.*, ua1.cus_id, ua2.cus_id
FROM transactions2 tr
LEFT JOIN account2 a1
ON tr.src_id = a1.acc_id
LEFT JOIN account2 a2
ON tr.rsv_id = a2.acc_id
LEFT JOIN userAccounts2 ua1
ON ua1.acc_id = src_id
LEFT JOIN userAccounts2 ua2
ON ua2.acc_id = rsv_id
LEFT JOIN customerClerks2 cc1
ON cc1.cus_id = ua1.cus_id
LEFT JOIN customerClerks2 cc2
ON cc2.cus_id = ua2.cus_id
WHERE cc2.clerk_id = 3 or cc2.clerk_id = 3;*/

SELECT DISTINCT tr.*, ua1.cus_id, ua2.cus_id
FROM transactions2 tr
LEFT JOIN account2 a1
ON tr.src_id = a1.acc_id
LEFT JOIN account2 a2
ON tr.rsv_id = a2.acc_id
LEFT JOIN userAccounts2 ua1
ON ua1.acc_id = src_id
LEFT JOIN userAccounts2 ua2
ON ua2.acc_id = rsv_id
WHERE ua1.cus_id = 302 or ua2.cus_id = 302;
