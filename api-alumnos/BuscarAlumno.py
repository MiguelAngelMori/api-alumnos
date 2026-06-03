import boto3

def lambda_handler(event, context):
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    alumno = response.get('Item', None)
    if alumno:
        return {
            'statusCode': 200,
            'alumno': alumno
        }
    else:
        return {
            'statusCode': 404,
            'mensaje': 'Alumno no encontrado'
        }
