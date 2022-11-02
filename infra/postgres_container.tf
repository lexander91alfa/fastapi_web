resource "docker_container" "postgres_container" {
  name    = "postgres_container"
  image   = docker_image.postgres.image_id
  restart = "always"

  env = local.environment

  ports {
    internal = "5432"
    external = "5432"
    ip       = "0.0.0.0"
  }

  volumes {
    container_path = "/var/lib/postgresql/data"
    host_path      = "${local.abs_path}/../db"
  }
}
