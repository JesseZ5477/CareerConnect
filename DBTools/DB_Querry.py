from CareerConnect.DBTools.DB_Utils import execute_query

# a function to use execute query to query resume files paths by job ID in mysql db
def get_candidates_file_paths(mydb, job_id):
    query = f"SELECT file_path FROM candidates WHERE job_id = {job_id}"
    results = execute_query(mydb, query).fetchall()
    return results

# a function to use execute query to query index path by job ID in mysql db
def get_index_path(mydb, job_id):    
    query = f"SELECT index_path FROM candidates WHERE job_id = {job_id}"
    results = execute_query(mydb, query).fetchall()
    return results

def get_attributes(mydb, job_id):
    ...

def set_attributes(mydb, job_id):
    ...
    
def post_match_score(mydb, resume_id, match_score, comment):
    query = f"UPDATE candidates SET match_score = {match_score}, comment = '{comment}' WHERE resume_id = {resume_id}"
    execute_query(mydb, query)