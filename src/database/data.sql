CREATE TABLE IF NOT EXISTS groups (
    id integer PRIMARY KEY,
    name text NOT NULL,
    description text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS services (
    id integer PRIMARY KEY,
    group_id integer NOT NULL,
    name text NOT NULL,
    service_url text NOT NULL DEFAULT '#',
    tag_name_1 text DEFAULT 'default_tag_1_x',
    tag_name_2 text DEFAULT 'default_tag_2_x',
    tag_name_3 text DEFAULT 'default_tag_3_x',
    description text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,  
    is_deleted integer DEFAULT 0,
    
    FOREIGN KEY(group_id) REFERENCES groups(id),
);


CREATE TABLE IF NOT EXISTS bulletin_types (
    id integer PRIMARY KEY,
    name text NOT NULL,
    description text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS bulletin_states (
    id integer PRIMARY KEY,
    name text NOT NULL,
    description text,
    color text DEFAULT '#000000',
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS bulletin_procedures (
    id integer PRIMARY KEY,
    name text NOT NULL,
    description text,
    tolist text,
    cclist text,
    bcclist text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS languages (
    id integer PRIMARY KEY,
    name text NOT NULL,
    short_name text NOT NULL,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS terms (
    id integer PRIMARY KEY,
    language_id integer NOT NULL,
    name text NOT NULL,
    value text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0,
    FOREIGN KEY(language_id) REFERENCES languages(id)
);
CREATE TABLE IF NOT EXISTS bulletins (
    id integer PRIMARY KEY,
    language_id integer NOT NULL,
    organization text NOT NULL,
    bulletin_type_id integer NOT NULL,
    bulletin_state_id integer NOT NULL,
    bulletin_classification text,
    bulletin_priority text,
    contact text,
    ticket_service_url text,
    ticket_service_user text,
    ticket_service_password text,
    ticket_support_group text,
    ticket_assigned_to text,
    ticket_case_url text DEFAULT '#',
    ticket_case_id text,
    media_service_url text NOT NULL,
    media_service_smtp text NOT NULL,
    media_service_port text NOT NULL,
    media_service_user text NOT NULL,
    media_service_password text NOT NULL,
    created_by text NOT NULL,
    code text NOT NULL,
    title text NOT NULL,
    detail text NOT NULL,
    effect text NOT NULL,
    begin_time datetime DEFAULT CURRENT_TIMESTAMP,
    end_time datetime DEFAULT CURRENT_TIMESTAMP,
    duration integer DEFAULT 0,
    bulletin_resolution text,
    root_cause text,
    resolved_time datetime DEFAULT CURRENT_TIMESTAMP, 
    resolved_by text,
    is_resolved integer DEFAULT 0,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP, 
    modify_time datetime DEFAULT CURRENT_TIMESTAMP,  
    is_deleted integer DEFAULT 0,
    
    FOREIGN KEY(language_id) REFERENCES languages(id),
    FOREIGN KEY(bulletin_type_id) REFERENCES bulletin_types(id),
    FOREIGN KEY(bulletin_state_id) REFERENCES bulletin_states(id)
);

CREATE TABLE IF NOT EXISTS groupped_bulletin_view (
    id integer PRIMARY KEY,
    bulletin_id integer NOT NULL,
    bulletin_type_id integer NOT NULL,
    bulletin_state_id integer NOT NULL,
    code text NOT NULL,
    duration integer DEFAULT 0,
    
	organization text NOT NULL,
    group_id integer NOT NULL,
    service_id integer NOT NULL,
    
    begin_time datetime DEFAULT CURRENT_TIMESTAMP,
    end_time datetime DEFAULT CURRENT_TIMESTAMP,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0,
    
    FOREIGN KEY(bulletin_id) REFERENCES bulletins(id),
    FOREIGN KEY(bulletin_type_id) REFERENCES bulletin_types(id),
    FOREIGN KEY(bulletin_state_id) REFERENCES bulletin_states(id),
    FOREIGN KEY(group_id) REFERENCES groups(id),
    FOREIGN KEY(service_id) REFERENCES services(id)
);

CREATE TABLE IF NOT EXISTS user_logs (
    id integer PRIMARY KEY,
    authentication_service_url text NOT NULL,
    user_id integer NOT NULL,
    type text NOT NULL,
    name text NOT NULL,
    description text,
    insert_time datetime DEFAULT CURRENT_TIMESTAMP,    
    is_deleted integer DEFAULT 0
);

INSERT INTO groups(id,name,description) VALUES(1,'webapplications','web applications');

INSERT INTO services(id,group_id,contact_id,name,service_url,tag_name_1,tag_name_2,tag_name_3,description) VALUES(1,1,1,'www.test1.com','http://www.test1.com','test1.com','default_tag_2_x','default_tag_3_y','description');
INSERT INTO services(id,group_id,contact_id,name,service_url,tag_name_1,tag_name_2,tag_name_3,description) VALUES(2,1,1,'www.test2.com','http://www.test2.com','test2.com','default_tag_2_x','default_tag_3_y','description');
INSERT INTO services(id,group_id,contact_id,name,service_url,tag_name_1,tag_name_2,tag_name_3,description) VALUES(3,1,1,'www.test3.com','http://www.test3.com','test3.com','default_tag_2_x','default_tag_3_y','description');

INSERT INTO bulletin_types(id,name,description) VALUES(1,'Planned Maintenance','description');
INSERT INTO bulletin_types(id,name,description) VALUES(2,'Urgent Maintenance','description');
INSERT INTO bulletin_types(id,name,description) VALUES(3,'Outage','description');
INSERT INTO bulletin_types(id,name,description) VALUES(4,'Alert','description');
INSERT INTO bulletin_types(id,name,description) VALUES(5,'Planned Deployment','description');
INSERT INTO bulletin_types(id,name,description) VALUES(6,'Urgent Deployment','description');

INSERT INTO bulletin_states(id,name,description,color) VALUES(1,'Scheduled','description','#ff851b');
INSERT INTO bulletin_states(id,name,description,color) VALUES(2,'Started','description','#f56954');
INSERT INTO bulletin_states(id,name,description,color) VALUES(3,'Canceled','description','#d2d6de');
INSERT INTO bulletin_states(id,name,description,color) VALUES(4,'Done','description','#00a65a');
INSERT INTO bulletin_states(id,name,description,color) VALUES(5,'RollBack','description','#605ca8');
INSERT INTO bulletin_states(id,name,description,color) VALUES(6,'WaitingforConfirmation','description','#f39c12');

INSERT INTO bulletin_procedures(id,name,description,tolist,cclist,bcclist) VALUES(1,'test procedure','description','oguzkaragoz@gmail.com','itmonitoringcommunity@gmail.com',NULL);


INSERT INTO languages(id,name,short_name) VALUES(1,'English','en');
INSERT INTO languages(id,name,short_name) VALUES(2,'Turkish','tr');
INSERT INTO languages(id,name,short_name) VALUES(3,'Russian','ru');

INSERT INTO terms(id,language_id,name,value) VALUES(1,1,'Bulletin.State.Scheduled','Scheduled');
INSERT INTO terms(id,language_id,name,value) VALUES(2,1,'Bulletin.State.Started','Started');
INSERT INTO terms(id,language_id,name,value) VALUES(3,1,'Bulletin.State.Canceled','Canceled');
INSERT INTO terms(id,language_id,name,value) VALUES(4,1,'Bulletin.State.Done','Done');
INSERT INTO terms(id,language_id,name,value) VALUES(5,1,'Bulletin.State.RollBack','RollBack');
INSERT INTO terms(id,language_id,name,value) VALUES(6,1,'Bulletin.State.WaitingforConfirmation','Waiting for Confirmation');
INSERT INTO terms(id,language_id,name,value) VALUES(7,1,'Bulletin.Type.PlannedMaintenance','Planned Maintenance');
INSERT INTO terms(id,language_id,name,value) VALUES(8,1,'Bulletin.Type.UrgentMaintenance','Urgent Maintenance');
INSERT INTO terms(id,language_id,name,value) VALUES(9,1,'Bulletin.Type.Outage','Outage');
INSERT INTO terms(id,language_id,name,value) VALUES(10,1,'Bulletin.Type.Alert','Alert');
INSERT INTO terms(id,language_id,name,value) VALUES(11,1,'Bulletin.Title','Title');
INSERT INTO terms(id,language_id,name,value) VALUES(12,1,'Bulletin.Detail','Detail');
INSERT INTO terms(id,language_id,name,value) VALUES(13,1,'Bulletin.Effect','Effect');
INSERT INTO terms(id,language_id,name,value) VALUES(14,1,'Bulletin.BeginTime','Begin Time');
INSERT INTO terms(id,language_id,name,value) VALUES(15,1,'Bulletin.EndTime','End Time');
INSERT INTO terms(id,language_id,name,value) VALUES(16,1,'Bulletin.Duration','Duration');
INSERT INTO terms(id,language_id,name,value) VALUES(17,1,'Bulletin.Priority','Priority');
INSERT INTO terms(id,language_id,name,value) VALUES(18,1,'Bulletin.Responsible','Responsible');
INSERT INTO terms(id,language_id,name,value) VALUES(19,1,'Bulletin.Procedure','Procedure');
INSERT INTO terms(id,language_id,name,value) VALUES(20,1,'Bulletin.CreatedBy','Created By');
INSERT INTO terms(id,language_id,name,value) VALUES(21,1,'Bulletin.Minute','Minutes');
INSERT INTO terms(id,language_id,name,value) VALUES(22,1,'Bulletin.CaseId','Case Id');
INSERT INTO terms(id,language_id,name,value) VALUES(23,1,'Bulletin.Undefined','Undefined');
INSERT INTO terms(id,language_id,name,value) VALUES(24,1,'Bulletin.Type','Bulletin Type');
INSERT INTO terms(id,language_id,name,value) VALUES(25,1,'Bulletin.Priority.Critical','Critical');
INSERT INTO terms(id,language_id,name,value) VALUES(26,1,'Bulletin.Priority.High','High');
INSERT INTO terms(id,language_id,name,value) VALUES(27,1,'Bulletin.Priority.Medium','Medium');
INSERT INTO terms(id,language_id,name,value) VALUES(28,1,'Bulletin.Priority.Low','Low');
INSERT INTO terms(id,language_id,name,value) VALUES(29,1,'Bulletin.State','State');
INSERT INTO terms(id,language_id,name,value) VALUES(30,1,'Bulletin.Type.PlannedDeployment','Planned Deployment');
INSERT INTO terms(id,language_id,name,value) VALUES(31,1,'Bulletin.Type.UrgentDeployment','Urgent Deployment');

--INSERT INTO bulletins(id,language_id,organization,bulletin_type_id,bulletin_state_id,bulletin_classification,bulletin_priority,contact,ticket_service_url,ticket_service_user,ticket_service_password,ticket_support_group,ticket_assigned_to,ticket_case_url,ticket_case_id,media_service_url,media_service_smtp,media_service_port,media_service_user,media_service_password,created_by,code,title,detail,effect,begin_time,end_time,duration,bulletin_resolution_id,root_cause,resolved_time,resolved_by,is_resolved) VALUES(1,1,'itmonitoringcommunity',1,'bulletin_classification','bulletin_priority','contact','ticket_service_url','ticket_service_user','ticket_support_group','ticket_service_password','ticket_assigned_to','ticket_case_url','ticket_case_id','media_service_url','media_service_smtp','media_service_port','media_service_user','media_service_password','created_by','code','title','detail','effect','2018-07-27 16:04:16','2018-07-27 16:24:16',0,'bulletin_resolution','root_cause','2018-07-27 16:04:16','resolved_by',0);
