# Beauty Tech Color System Documentation

## Overview
Comprehensive color management system for virtual makeup try-on products, ensuring accurate color representation across different skin tones, lighting conditions, and product textures.

## Lipstick Color Database

### Premium Color Collection

#### Unicorn Red Collection
**Primary RGB**: (255, 20, 147)
- **HEX**: #FF1493
- **HSL**: 330°, 100%, 54%
- **Color Family**: Pink-Red
- **Undertone**: Cool magenta
- **Opacity**: 95%
- **Finish Compatibility**: Matte, Satin, Shimmer
- **Skin Tone Range**: Universal (fair to deep)
- **Lighting Adaptation**: Excellent (maintains vibrancy in all conditions)

**Technical Specifications**:
- **Lab Values**: L*: 54, a*: 80, b*: 20
- **Pantone Match**: 218 C
- **NCS Code**: 1070-R50B
- **Delta E Tolerance**: ≤2.0

#### Classic Red Collection
**Primary RGB**: (220, 20, 60)
- **HEX**: #DC143C
- **Color Family**: True Red
- **Undertone**: Neutral-warm
- **Best For**: Fair to medium skin tones
- **Cultural Significance**: Timeless, professional

#### Hot Pink Collection
**Primary RGB**: (255, 105, 180)
- **HEX**: #FF69B4
- **Color Family**: Pink
- **Undertone**: Blue-pink
- **Best For**: Cool undertones
- **Trend Status**: Seasonal (Spring/Summer)

### Color Validation Matrix

| Color Name | RGB Values | Skin Tone | Lighting | Texture | Score |
|------------|------------|-----------|----------|---------|-------|
| Unicorn Red | (255,20,147) | Universal | All | All | 9.5/10 |
| Classic Red | (220,20,60) | Fair-Medium | Natural | Matte | 8.8/10 |
| Hot Pink | (255,105,180) | Cool | Bright | Shimmer | 8.2/10 |

## Foundation Color System

### Undertone Classification
- **Cool**: Blue/pink undertones
- **Warm**: Yellow/golden undertones
- **Neutral**: Balanced undertones

### Shade Range (Fitzpatrick Scale)
| Fitzpatrick | Shade Range | RGB Examples |
|-------------|-------------|--------------|
| I-II | Porcelain-Light | (255,248,220) - (245,245,220) |
| III-IV | Light-Medium | (222,184,135) - (210,180,140) |
| V-VI | Medium-Deep | (139,69,19) - (101,67,33) |

## Color Processing Pipeline

### 1. Color Extraction
- **Input**: 2000x2000px product images
- **Method**: Computer vision algorithms + manual validation
- **Output**: Dominant RGB + color palette (5-7 shades)
- **Accuracy**: ±1% variance tolerance

### 2. Lighting Calibration
- **Indoor Lighting**: 5000K LED simulation
- **Outdoor Lighting**: 6500K daylight simulation
- **Low Light**: 2700K warm white simulation
- **Adjustment Range**: ±15% brightness compensation

### 3. Skin Tone Matching
- **Algorithm**: CIELAB color space conversion
- **Delta E Calculation**: ≤3.0 acceptable match
- **Auto-correction**: Shifts toward complementary skin tones
- **Validation**: Tested on 50+ diverse skin tone samples

### 4. Texture Integration
- **Matte Finish**: -10% brightness reduction
- **Satin Finish**: No adjustment
- **Shimmer Finish**: +5% brightness increase
- **Glitter Finish**: +15% brightness increase

## Quality Assurance Protocols

### Pre-Launch Validation
- [x] RGB accuracy verified against physical samples
- [x] Cross-platform rendering consistency (iOS/Android/Web)
- [x] Performance impact assessed (<50ms load time)
- [x] Accessibility compliance (color contrast ratios)

### Production Monitoring
- **Daily Checks**: Automated color validation pipeline
- **Weekly Reviews**: Manual spot-checks on new products
- **Monthly Audits**: Full color database integrity verification
- **Issue Response**: 24-hour SLA for color-related bugs

## Troubleshooting Guide

### Common Color Issues

**Problem**: Color appears different on different devices
**Solution**: Check color space conversion, verify ICC profiles

**Problem**: Color shifts in low lighting
**Solution**: Increase base brightness by 8-12%, check gamma correction

**Problem**: Color doesn't match physical product
**Solution**: Re-scan product image, verify white balance, check lighting setup

**Problem**: Performance issues with color loading
**Solution**: Optimize texture compression, reduce color palette size, implement lazy loading

## Technical Architecture

### Color Storage
- **Database**: PostgreSQL with JSONB color profiles
- **Caching**: Redis for frequently accessed colors
- **Backup**: Daily snapshots with version control

### API Endpoints
- `GET /api/colors/{product_id}` - Retrieve color profile
- `POST /api/colors/validate` - Validate new color submission
- `PUT /api/colors/{id}/adjust` - Update color parameters

## Best Practices

1. **Always test on multiple skin tones** before finalizing RGB values
2. **Use calibrated monitors** (Delta E <2.0) for color work
3. **Document lighting conditions** for all color captures
4. **Include fallback colors** for edge cases
5. **Regular calibration** of capture equipment (monthly)

