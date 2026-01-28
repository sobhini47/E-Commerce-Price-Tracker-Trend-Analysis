import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Flipkart Earbuds Analysis",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div[data-testid="metric-container"] label {
        color: white !important;
        font-weight: bold;
    }
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: white !important;
        font-size: 2em;
    }
    h1, h2, h3 {
        color: #2d3748;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🎧 Flipkart Earbuds Analysis Dashboard")
st.markdown("### Interactive analysis of your web-scraped earbud data")
st.markdown("---")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_data_cleaned.csv")
    df['Brand'] = df['Product Name'].str.split().str[0]
    return df

try:
    df = load_data()
    
    # Sidebar Navigation
    st.sidebar.title("📊 Navigation")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "Select Analysis:",
        ["🏠 Overview", "💰 Price Analysis", "⭐ Rating Analysis", 
         "📈 Price vs Rating", "🏆 Top Rated", "💸 Best Budget", "🏢 Brand Analysis"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"**Total Products:** {len(df)}")
    st.sidebar.success(f"**Brands:** {df['Brand'].nunique()}")
    
    # ==================== OVERVIEW PAGE ====================
    if page == "🏠 Overview":
        st.header("📊 Dashboard Overview")
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Products", len(df))
        with col2:
            st.metric("Avg Price", f"₹{df['Price'].mean():.0f}")
        with col3:
            st.metric("Avg Rating", f"{df['Rating'].mean():.2f} ⭐")
        with col4:
            st.metric("Top Rating", f"{df['Rating'].max():.1f} ⭐")
        
        st.markdown("---")
        
        # Two columns layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📦 Dataset Preview")
            st.dataframe(df.head(10), use_container_width=True, height=400)
        
        with col2:
            st.subheader("📈 Quick Statistics")
            stats_df = df[['Price', 'Rating']].describe()
            st.dataframe(stats_df, use_container_width=True)
            
            st.markdown("### 🎯 Key Insights")
            st.info(f"💰 **Price Range:** ₹{df['Price'].min():.0f} - ₹{df['Price'].max():.0f}")
            st.success(f"⭐ **Products with 4+ Rating:** {len(df[df['Rating'] >= 4.0])}")
            st.warning(f"💸 **Budget Options (<₹800, Rating ≥4.0):** {len(df[(df['Price'] < 800) & (df['Rating'] >= 4.0)])}")
    
    # ==================== PRICE ANALYSIS ====================
    elif page == "💰 Price Analysis":
        st.header("💰 Price Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Price Distribution")
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.hist(df['Price'], bins=15, color='#667eea', edgecolor='black', alpha=0.7)
            ax.set_xlabel("Price (₹)", fontsize=12, fontweight='bold')
            ax.set_ylabel("Number of Products", fontsize=12, fontweight='bold')
            ax.set_title("Price Distribution of Flipkart Earbuds", fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            st.pyplot(fig)
        
        with col2:
            st.subheader("📈 Price Statistics")
            st.dataframe(df['Price'].describe(), use_container_width=True)
            
            st.markdown("### 💡 Price Insights")
            st.metric("Minimum Price", f"₹{df['Price'].min():.0f}")
            st.metric("Maximum Price", f"₹{df['Price'].max():.0f}")
            st.metric("Median Price", f"₹{df['Price'].median():.0f}")
            st.metric("Standard Deviation", f"₹{df['Price'].std():.0f}")
        
        st.markdown("---")
        
        # Box Plot
        st.subheader("📦 Price Distribution Box Plot")
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.boxplot(df['Price'], vert=False, patch_artist=True,
                   boxprops=dict(facecolor='#667eea', alpha=0.7),
                   medianprops=dict(color='red', linewidth=2))
        ax.set_xlabel("Price (₹)", fontsize=12, fontweight='bold')
        ax.set_title("Price Distribution Box Plot", fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        st.pyplot(fig)
    
    # ==================== RATING ANALYSIS ====================
    elif page == "⭐ Rating Analysis":
        st.header("⭐ Rating Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Rating Distribution")
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.hist(df['Rating'], bins=10, color='#f6ad55', edgecolor='black', alpha=0.7)
            ax.set_xlabel("Rating", fontsize=12, fontweight='bold')
            ax.set_ylabel("Number of Products", fontsize=12, fontweight='bold')
            ax.set_title("Rating Distribution of Flipkart Earbuds", fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            st.pyplot(fig)
        
        with col2:
            st.subheader("📈 Rating Statistics")
            st.dataframe(df['Rating'].describe(), use_container_width=True)
            
            st.markdown("### 💡 Rating Insights")
            st.metric("Minimum Rating", f"{df['Rating'].min():.1f} ⭐")
            st.metric("Maximum Rating", f"{df['Rating'].max():.1f} ⭐")
            st.metric("Median Rating", f"{df['Rating'].median():.1f} ⭐")
            st.metric("Products with 4+ Rating", len(df[df['Rating'] >= 4.0]))
        
        st.markdown("---")
        
        # Rating Categories
        st.subheader("🎯 Rating Categories")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            excellent = len(df[df['Rating'] >= 4.5])
            st.info(f"**Excellent (≥4.5):** {excellent} products")
        with col2:
            good = len(df[(df['Rating'] >= 4.0) & (df['Rating'] < 4.5)])
            st.success(f"**Good (4.0-4.5):** {good} products")
        with col3:
            average = len(df[df['Rating'] < 4.0])
            st.warning(f"**Average (<4.0):** {average} products")
    
    # ==================== PRICE VS RATING ====================
    elif page == "📈 Price vs Rating":
        st.header("📈 Price vs Rating Analysis")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        scatter = ax.scatter(df['Price'], df['Rating'], 
                           c=df['Price'], cmap='viridis', 
                           s=100, alpha=0.6, edgecolors='black')
        ax.set_xlabel("Price (₹)", fontsize=12, fontweight='bold')
        ax.set_ylabel("Rating", fontsize=12, fontweight='bold')
        ax.set_title("Price vs Rating Scatter Plot", fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.colorbar(scatter, ax=ax, label='Price (₹)')
        st.pyplot(fig)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Correlation Analysis")
            correlation = df['Price'].corr(df['Rating'])
            st.metric("Correlation Coefficient", f"{correlation:.3f}")
            
            if correlation > 0.5:
                st.success("Strong positive correlation - Higher prices tend to have higher ratings")
            elif correlation > 0.2:
                st.info("Moderate positive correlation")
            elif correlation > -0.2:
                st.warning("Weak or no correlation")
            else:
                st.error("Negative correlation - Higher prices have lower ratings")
        
        with col2:
            st.subheader("💡 Key Insights")
            high_value = df[(df['Price'] < df['Price'].median()) & (df['Rating'] >= 4.0)]
            st.success(f"**High Value Products:** {len(high_value)} products with below-median price and 4+ rating")
            
            premium_good = df[(df['Price'] > df['Price'].quantile(0.75)) & (df['Rating'] >= 4.0)]
            st.info(f"**Premium Quality:** {len(premium_good)} high-priced products with 4+ rating")
    
    # ==================== TOP RATED ====================
    elif page == "🏆 Top Rated":
        st.header("🏆 Top Rated Products")
        
        top_n = st.slider("Select number of top products to display:", 5, 20, 10)
        
        top_rated = df.sort_values(by="Rating", ascending=False).head(top_n)
        
        st.subheader(f"🌟 Top {top_n} Rated Products")
        
        # Display with custom styling
        for idx, row in top_rated.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**{row['Product Name']}**")
            with col2:
                st.markdown(f"**₹{row['Price']:.0f}**")
            with col3:
                st.markdown(f"**{row['Rating']} ⭐**")
            st.markdown("---")
        
        # Visualization
        st.subheader("📊 Top Rated Products Visualization")
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.barh(top_rated['Product Name'].str[:30], top_rated['Rating'], 
                       color='#48bb78', edgecolor='black', alpha=0.7)
        ax.set_xlabel("Rating", fontsize=12, fontweight='bold')
        ax.set_ylabel("Product Name", fontsize=12, fontweight='bold')
        ax.set_title(f"Top {top_n} Rated Products", fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        st.pyplot(fig)
    
    # ==================== BEST BUDGET ====================
    elif page == "💸 Best Budget":
        st.header("💸 Best Budget Products")
        
        col1, col2 = st.columns(2)
        with col1:
            max_price = st.slider("Maximum Price (₹):", 300, 2000, 800, step=50)
        with col2:
            min_rating = st.slider("Minimum Rating:", 3.0, 5.0, 4.0, step=0.1)
        
        best_budget = df[(df['Price'] <= max_price) & (df['Rating'] >= min_rating)]
        best_budget = best_budget.sort_values(by="Rating", ascending=False)
        
        st.subheader(f"🎯 Found {len(best_budget)} products matching your criteria")
        
        if len(best_budget) > 0:
            # Display products
            for idx, row in best_budget.iterrows():
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{row['Product Name']}**")
                with col2:
                    st.markdown(f"**₹{row['Price']:.0f}**")
                with col3:
                    st.markdown(f"**{row['Rating']} ⭐**")
                st.markdown("---")
            
            # Visualization
            st.subheader("📊 Budget Products Distribution")
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.scatter(best_budget['Price'], best_budget['Rating'], 
                      s=150, alpha=0.6, c='#38b2ac', edgecolors='black')
            ax.set_xlabel("Price (₹)", fontsize=12, fontweight='bold')
            ax.set_ylabel("Rating", fontsize=12, fontweight='bold')
            ax.set_title("Best Budget Products - Price vs Rating", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
        else:
            st.warning("No products found matching your criteria. Try adjusting the filters.")
    
    # ==================== BRAND ANALYSIS ====================
    elif page == "🏢 Brand Analysis":
        st.header("🏢 Brand-wise Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("⭐ Average Rating per Brand")
            brand_rating = df.groupby('Brand')['Rating'].mean().sort_values(ascending=False)
            st.dataframe(brand_rating, use_container_width=True)
            
            # Visualization
            fig, ax = plt.subplots(figsize=(8, 6))
            brand_rating.plot(kind='barh', ax=ax, color='#f6ad55', edgecolor='black', alpha=0.7)
            ax.set_xlabel("Average Rating", fontsize=12, fontweight='bold')
            ax.set_ylabel("Brand", fontsize=12, fontweight='bold')
            ax.set_title("Average Rating by Brand", fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            st.pyplot(fig)
        
        with col2:
            st.subheader("💰 Average Price per Brand")
            brand_price = df.groupby('Brand')['Price'].mean().sort_values(ascending=False)
            st.dataframe(brand_price, use_container_width=True)
            
            # Visualization
            fig, ax = plt.subplots(figsize=(8, 6))
            brand_price.plot(kind='barh', ax=ax, color='#667eea', edgecolor='black', alpha=0.7)
            ax.set_xlabel("Average Price (₹)", fontsize=12, fontweight='bold')
            ax.set_ylabel("Brand", fontsize=12, fontweight='bold')
            ax.set_title("Average Price by Brand", fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            st.pyplot(fig)
        
        st.markdown("---")
        
        # Product count by brand
        st.subheader("📦 Product Count by Brand")
        brand_count = df['Brand'].value_counts()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        brand_count.plot(kind='bar', ax=ax, color='#48bb78', edgecolor='black', alpha=0.7)
        ax.set_xlabel("Brand", fontsize=12, fontweight='bold')
        ax.set_ylabel("Number of Products", fontsize=12, fontweight='bold')
        ax.set_title("Product Count by Brand", fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

except FileNotFoundError:
    st.error("❌ **Error:** `ecommerce_data_cleaned.csv` file not found!")
    st.info("Please make sure your CSV file is in the same directory as this script.")
except Exception as e:
    st.error(f"❌ **Error:** {str(e)}")
    st.info("Please check your CSV file format and ensure it has 'Product Name', 'Price', and 'Rating' columns.")