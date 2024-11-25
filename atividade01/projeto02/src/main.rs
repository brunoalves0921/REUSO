use projeto01::{back_of_house::take_care_trash, front_of_house::{hosting::{add_to_wait_list, seat_at_table}, serving::{serve_order, take_order, take_payment}}, pi::PI};

fn main() {
    add_to_wait_list();
    seat_at_table();
    take_order();
    serve_order();
    take_payment();
    take_care_trash();

    println!("PI: {}", PI);
}
