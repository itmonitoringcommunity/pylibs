CREATE TABLE IF NOT EXISTS bulletins (
    id integer PRIMARY KEY,
    
    type text NOT NULL,
    priority text,
    state text NOT NULL,

    ticket_case_url text DEFAULT '#',
    ticket_case_id text,
    
    created_by text NOT NULL,
    code text NOT NULL,
    title text NOT NULL,
    detail text NOT NULL,
    effect text NOT NULL,
    contact text,
    
    begin_time datetime DEFAULT CURRENT_TIMESTAMP,
    end_time datetime DEFAULT CURRENT_TIMESTAMP,
    duration integer DEFAULT 0,
    
    insert_time datetime DEFAULT CURRENT_TIMESTAMP, 
    modify_time datetime DEFAULT CURRENT_TIMESTAMP,  
    is_deleted integer DEFAULT 0

);

INSERT INTO bulletins(id,type,priority,state,
ticket_case_url,ticket_case_id,created_by,
code,title,detail,effect,begin_time,end_time,duration) 
VALUES(1,'Planned Maintenance','Medium','Scheduled','#','PM120023','admin',
'BLT20023','Test Bakımı','13:00 da sql db bakımı yapılacaktır.','local services','2020-04-02 13:00:00','2020-04-02 14:20:00',80);

INSERT INTO bulletins(id,type,priority,state,
ticket_case_url,ticket_case_id,created_by,
code,title,detail,effect,begin_time,end_time,duration) 
VALUES(2,'Planned Maintenance','Medium','Scheduled','#','PM120024','admin',
'BLT20024','Test Bakımı','13:00 da sql db bakımı yapılacaktır.','local services','2020-04-02 13:00:00','2020-04-02 14:20:00',80);

INSERT INTO bulletins(id,type,priority,state,
ticket_case_url,ticket_case_id,created_by,
code,title,detail,effect,begin_time,end_time,duration) 
VALUES(3,'Planned Maintenance','Medium','Scheduled','#','PM120025','admin',
'BLT20025','Test Bakımı','13:00 da sql db bakımı yapılacaktır.','local services','2020-04-02 13:00:00','2020-04-02 14:20:00',80);
