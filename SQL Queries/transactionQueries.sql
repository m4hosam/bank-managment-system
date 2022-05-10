--all transactions + the source and recieve balances
SELECT tr.* , a1.balance src_balance, a2.balance rsv_balance 
FROM transactions2 tr 
LEFT JOIN account2 a1
ON tr.src_id = a1.acc_id
LEFT JOIN account2 a2
ON tr.rsv_id = a2.acc_id;

--transactions where the recieve is null + the source's balance
SELECT trans_no, trans_date, src_id, ua2.cus_id, trans_type, total, a1.balance src_balance
FROM transactions2 tr 
LEFT JOIN account2 a1
ON tr.src_id = a1.acc_id
LEFT JOIN userAccounts2 ua2
ON ua2.acc_id = tr.src_id
WHERE tr.rsv_id IS NULL;

--transactions where the source is null + the recieve's balance
SELECT trans_no, trans_date, ua2.cus_id, rsv_id, trans_type, total, a1.balance rsv_balance
FROM transactions2 tr 
LEFT JOIN account2 a1
ON tr.rsv_id = a1.acc_id
LEFT JOIN userAccounts2 ua2
ON ua2.acc_id = tr.rsv_id
WHERE tr.src_id IS NULL;
