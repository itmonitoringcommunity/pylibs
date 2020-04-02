CREATE TABLE IF NOT EXISTS bulletins (
    id integer PRIMARY KEY,
    
    type text NOT NULL,
    priority text,
    state text NOT NULL,
    color text,

    created_by text NOT NULL,
    code text NOT NULL,
    title text NOT NULL,
    detail text NOT NULL,
    effect text NOT NULL,
    contact text,
    
    begin_time datetime DEFAULT CURRENT_TIMESTAMP,
    end_time datetime DEFAULT CURRENT_TIMESTAMP,
    duration integer DEFAULT 0,

    ticket_case_url text DEFAULT '#',
    ticket_case_id text,

    resolved_time datetime DEFAULT CURRENT_TIMESTAMP, 
    is_resolved integer DEFAULT 0,
    resolved_by text,
    temporary_solution text,
    permanent_solution text,
    root_cause text,
    
    insert_time datetime DEFAULT CURRENT_TIMESTAMP, 
    modify_time datetime DEFAULT CURRENT_TIMESTAMP,  
    is_deleted integer DEFAULT 0
);

INSERT INTO bulletins(id,type,priority,state,color,
created_by,code,title,detail,effect,contact,
begin_time,end_time,duration,
ticket_case_url,ticket_case_id,
is_resolved, resolved_by, temporary_solution, permanent_solution, root_cause
) 
VALUES(1,'Planned Maintenance','Medium','Scheduled','#',
'admin','BLT20023','Test Bakımı','13:00 da sql db bakımı yapılacaktır.','local services','oguzkaragoz@gmail.com',
'2020-04-02 13:00:00','2020-04-02 14:20:00',80,
'#','PM120023',
0,'admin','temporary_solution','permanent_solution','root_cause'
);
