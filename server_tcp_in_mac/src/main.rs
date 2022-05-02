use std::net::{self, SocketAddrV4};
fn main() {
    println!("Hello, world!");
}

struct Client {
    Name: &'static str,
    Adress: &'static str,
    socket: net::SocketAddrV4

}

struct Server {
    adress: net::Ipv4Addr,
    clients: Vec<(&'static str, )>,
}
