import json
import unittest
from app import app
# set our application to testing mode
app.testing = True


class TestApi(unittest.TestCase):
    def test_maximo_rectangulo_solver(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "1 0 0 0 \n0 0 0 0 \n1 0 0 0"
            result = client.post(
                '/maximo_rectangulo',
                data=sent
            )
            # check result from server with expected data
            ans_list = [int(x) for x in json.loads(result.data.decode("utf-8"))]
            self.assertEqual(
                ans_list,
                [0,1,3,3]
            )

    def test_maximo_cuadrado_solver(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "1 0 0 0 \n0 0 0 0 \n1 0 0 0"
            result = client.post(
                '/maximo_cuadrado',
                data=sent
            )
            # check result from server with expected data
            ans_list = [int(x) for x in json.loads(result.data.decode("utf-8"))]
            self.assertEqual(
                ans_list,
                [0,1,3]
            )

    def test_celdas_libres_false(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "1 1\n1 0 0 0 \n0 0 0 0 \n1 0 0 0"
            result = client.post(
                '/iterador_celdas_libres',
                data=sent
            )
            # check result from server with expected data
            self.assertEqual(
                [False], json.loads(result.data.decode("utf-8"))
            )

    def test_celdas_libres(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "1 2\n1 0 0 0 \n0 0 0 0 \n1 0 0 0"
            result = client.post(
                '/iterador_celdas_libres',
                data=sent
            )
            # check result from server with expected data
            ans_list = [[int(x) for x in y] for y in json.loads(result.data.decode("utf-8"))]
            print(ans_list)
            self.assertEqual(
                ans_list,[[1,2],[1,3],[0,2],[0,2],[0,3],[2,3],[2,2]])

class TestApi(unittest.TestCase):
    def test_maximo_rectangulo_solver(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "0 1 0 0 0 0 0 1 0 0 \n1 0 0 0 0 1 0 0 0 0 \n0 0 1 0 1 0 0 0 0 0 \n1 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 1 0 \n 0 0 0 0 0 0 0 0 0 0 \n" \
                   "0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 1 \n1 0 0 0 1 0 1 0 0 0 \n0 0 1 0 0 0 0 0 1 0 \n0 0 0 1 0 0 1 0 0 0"
            result = client.post(
                '/maximo_rectangulo',
                data=sent
            )
            # check result from server with expected data
            ans_list = [int(x) for x in json.loads(result.data.decode("utf-8"))]
            self.assertEqual(
                ans_list,
                [3,1,7,4]
            )

    def test_maximo_cuadrado_solver(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "0 1 0 0 0 0 0 1 0 0 \n1 0 0 0 0 1 0 0 0 0 \n0 0 1 0 1 0 0 0 0 0 \n1 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 1 0 \n 0 0 0 0 0 0 0 0 0 0 \n" \
                   "0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 1 \n1 0 0 0 1 0 1 0 0 0 \n0 0 1 0 0 0 0 0 1 0 \n0 0 0 1 0 0 1 0 0 0"
            result = client.post(
                '/maximo_cuadrado',
                data=sent
            )
            # check result from server with expected data
            ans_list = [int(x) for x in json.loads(result.data.decode("utf-8"))]
            self.assertEqual(
                ans_list,
                [3,1,4]
            )

    def test_celdas_libres_false(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = "0 1 0 0 0 0 0 1 0 0 \n1 0 0 0 0 1 0 0 0 0 \n0 0 1 0 1 0 0 0 0 0 \n1 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 1 0 \n 0 0 0 0 0 0 0 0 0 0 \n" \
                   "0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 1 \n1 0 0 0 1 0 1 0 0 0 \n0 0 1 0 0 0 0 0 1 0 \n0 0 0 1 0 0 1 0 0 0"
            result = client.post(
                '/iterador_celdas_libres',
                data=sent
            )
            # check result from server with expected data
            self.assertEqual(
                [False], json.loads(result.data.decode("utf-8"))
            )

