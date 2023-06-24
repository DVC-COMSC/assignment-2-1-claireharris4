def main():
    males = int(input('Enter the number of males in class:'))
    females = int(input('Enter the number of females in class:'))

    class_size = males + females
    m_perc = (males/class_size) *100
    f_perc = (females/class_size) *100

    print (f'The total number of students: \t \t {class_size}')
    print (f'The number of males and females: \t {males} \t \t {females}')
    print (f'The percentage of males and females: \t {m_perc:.2f}% \t {f_perc:.2f}%')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
