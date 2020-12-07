from neo4j import GraphDatabase
import json

class Model:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        
    def create_kurasi(self):
        with self.driver.session() as session:
            result = session.run("CREATE (a:Person { name:'web,static',email:'verlaily.ratu@gmail.com',judul:'hukum newton',kategori:'1',pelajaran:'Fisika',kelas:'X',link:'ada'  } ) RETURN id(a) AS node_id")
            record = result.single()
            return record["node_id"]
            
    def get_kurasi(self):
        data = []
        with self.driver.session() as session:
            #result = session.run("MATCH (p:Person) RETURN p.name as name, p.kategori as kategori, p.judul as judul, p.email as email, p.pelajaran as pelajaran, p.kelas as kelas, p.link as link")
            result = session.run("MATCH (a:DBM {site:'Curated'})-[:`CHILD_ID:`]->(b:ID)-[:`Nama:`]->(d:Nama),(b:ID)-[:`Email:`]->(e:Email), (b:ID)-[:`Judul:`]->(f:Judul), (b:ID)-[:`Kelas:`]->(g:Kelas),(b:ID)-[:`Pelajaran:`]->(h:Pelajaran),(b:ID)-[:`Kategori:`]->(i:Kategori), (b:ID)-[:`Link:`]->(j:Link) RETURN a,b.uid as id, d.nama as nama, e.email as email, f.judul as judul, g.kelas as kelas, h.pelajaran as pelajaran, i.kategori as kategori, j.link as link")
            values = []
            for record in result:
                values.append(record.values())
            return values

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

   