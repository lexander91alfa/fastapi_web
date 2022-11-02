resource "docker_image" "postgres" {
  name         = "postgres:latest"
  keep_locally = true
}
