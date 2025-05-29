# 使用Neo4j记录数据流转路径
from neo4j import GraphDatabase

class DataLineageTracker:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://gdpr-neo4j:7687")

    def log_operation(self, operation_type, data_id, node_ip):
        with self.driver.session() as session:
            session.write_transaction(
                self._create_operation_log,
                operation_type,
                data_id,
                node_ip
            )

    @staticmethod
    def _create_operation_log(tx, op_type, data_id, node_ip):
        query = (
            "MERGE (d:Data {id: $data_id}) "
            "CREATE (op:Operation {type: $op_type, time: datetime()}) "
            "CREATE (d)-[:HAS_OPERATION]->(op) "
            "CREATE (op)-[:EXECUTED_ON]->(n:Node {ip: $node_ip})"
        )
        tx.run(query, data_id=data_id, op_type=op_type, node_ip=node_ip)
