import matplotlib.pyplot as plt
import numpy as np

def calculate_tco(years, price, fuel_per_h, fuel_cost, maintenance_yr, work_h_yr):
    """
    Calculate Total Cost of Ownership (TCO) over a given period.
    """
    total_costs = []
    cumulative_cost = price
    for year in range(1, years + 1):
        annual_fuel = fuel_per_h * fuel_cost * work_h_yr
        annual_cost = annual_fuel + maintenance_yr
        cumulative_cost += annual_cost
        total_costs.append(cumulative_cost)
    return total_costs

def run_simulation():
    # Simulation Parameters
    years = 10
    work_h_yr = 1000  # Annual working hours
    
    # 1. Diesel Tractor (e.g., LS MT7)
    d_price = 80000000       # 80M KRW
    d_fuel_per_h = 15        # 15 L/h
    d_fuel_cost = 1800       # 1,800 KRW/L
    d_maint_yr = 2000000     # 2M KRW/yr (Oil, Filters, Urea)
    
    # 2. Electric Tractor (e.g., Monarch MK-V)
    e_price = 120000000      # 120M KRW
    e_elec_per_h = 20        # 20 kWh/h
    e_elec_cost = 200        # 200 KRW/kWh
    e_maint_yr = 500000      # 0.5M KRW/yr (Minimal maintenance)

    # Calculation
    diesel_tco = calculate_tco(years, d_price, d_fuel_per_h, d_fuel_cost, d_maint_yr, work_h_yr)
    electric_tco = calculate_tco(years, e_price, e_elec_per_h, e_elec_cost, e_maint_yr, work_h_yr)
    
    # Timeline
    timeline = np.arange(1, years + 1)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(timeline, diesel_tco, label='Diesel Tractor TCO', marker='o', color='red')
    plt.plot(timeline, electric_tco, label='Electric Tractor TCO', marker='s', color='blue')
    
    plt.title('10-Year TCO Comparison: Diesel vs Electric Tractor')
    plt.xlabel('Years of Operation')
    plt.ylabel('Cumulative Cost (KRW)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Find break-even point
    for i in range(years):
        if electric_tco[i] < diesel_tco[i]:
            print(f"[*] Electric tractor becomes more economical at Year {i+1}")
            plt.annotate('Break-even Point', xy=(i+1, electric_tco[i]), xytext=(i+2, electric_tco[i]-10000000),
                         arrowprops=dict(facecolor='black', shrink=0.05))
            break

    plt.tight_layout()
    plt.show()
    
    print("\n--- Final TCO Report (10 Years) ---")
    print(f"Diesel Overall Cost:   {diesel_tco[-1]:,.0f} KRW")
    print(f"Electric Overall Cost: {electric_tco[-1]:,.0f} KRW")
    print(f"Net Savings:           {diesel_tco[-1] - electric_tco[-1]:,.0f} KRW")

if __name__ == "__main__":
    run_simulation()
