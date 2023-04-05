def test_get_server(client):
    response = client.get(
        '/',
    )

    assert response.status_code == 200


def test_auth_principal_invalid_header(client, h_student_3):
    """
    failure case: invalid set of headers captured in auth decorator
    """
    response = client.get('/student/assignments', headers=h_student_3)
    assert response.status_code == 401
    assert response.json["message"] == "principal not found"


def test_auth_principal_cross_path_1(client, h_teacher_1):
    """
    failure case: invalid data access by teacher request
    """
    response = client.get('/student/assignments', headers=h_teacher_1)
    assert response.status_code == 403
    assert response.json["message"] == "requester should be a student"


def test_auth_principal_cross_path_2(client, h_student_1):
    """
    failure case: invalid access by student request
    """
    response = client.get('/teacher/assignments', headers=h_student_1)
    assert response.status_code == 403
    assert response.json["message"] == "requester should be a teacher"