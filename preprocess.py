import pandas as pd

def load_and_convert_to_text(csv_path):
    df = pd.read_csv(csv_path)
    texts = []

    for _, row in df.iterrows():
        gender = row['Gender']
        income = row['ApplicantIncome']
        area = row['Property_Area']
        education = row['Education']
        credit = "has" if row['Credit_History'] == 1.0 else "does not have"
        loan_amount = row['LoanAmount']
        status = "Approved ✅" if row['Loan_Status'] == "Y" else "Rejected ❌"

        doc = (
            f"{gender} applicant with {education} background and monthly income of ₹{income}, "
            f"from a {area.lower()} area, {credit} a credit history. "
            f"Requested loan amount of ₹{loan_amount}. Loan application was **{status}**."
        )
        texts.append(doc)
    
    return texts, df

